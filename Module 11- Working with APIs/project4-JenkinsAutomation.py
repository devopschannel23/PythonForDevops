import os
import time
import requests


JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
JENKINS_JOB = os.getenv("JENKINS_JOB")


def validate_config():
    required = {
        "JENKINS_URL": JENKINS_URL,
        "JENKINS_USER": JENKINS_USER,
        "JENKINS_TOKEN": JENKINS_TOKEN,
        "JENKINS_JOB": JENKINS_JOB,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise RuntimeError(
            f"Missing environment variables: {', '.join(missing)}"
        )


def get_session():
    session = requests.Session()

    session.auth = (
        JENKINS_USER,
        JENKINS_TOKEN
    )

    return session


def check_jenkins(session):
    url = f"{JENKINS_URL}/api/json"

    response = session.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    print("Jenkins connection successful")
    print(
        "Jenkins version:",
        response.headers.get("X-Jenkins", "Unknown")
    )


def trigger_build(session):
    url = (
        f"{JENKINS_URL}/job/"
        f"{JENKINS_JOB}/build"
    )

    response = session.post(
        url,
        timeout=10
    )

    response.raise_for_status()

    print("Build triggered successfully")

    return response


def get_queue_item_url(response):
    location = response.headers.get("Location")

    if not location:
        raise RuntimeError(
            "Jenkins did not return a queue location."
        )

    return location


def wait_for_build_number(session, queue_url):
    api_url = f"{queue_url}api/json"

    while True:
        response = session.get(
            api_url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("cancelled"):
            raise RuntimeError(
                "Jenkins queue item was cancelled."
            )

        executable = data.get("executable")

        if executable:
            build_number = executable["number"]

            print(
                f"Build number: #{build_number}"
            )

            return build_number

        print("Waiting for Jenkins to start the build...")
        time.sleep(3)


def monitor_build(session, build_number):
    url = (
        f"{JENKINS_URL}/job/"
        f"{JENKINS_JOB}/"
        f"{build_number}/api/json"
    )

    while True:
        response = session.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        building = data.get("building")
        result = data.get("result")

        print(
            f"Build #{build_number} | "
            f"Building: {building} | "
            f"Result: {result}"
        )

        if not building:
            return result

        time.sleep(5)


def main():
    validate_config()

    session = get_session()

    check_jenkins(session)

    response = trigger_build(session)

    queue_url = get_queue_item_url(response)

    build_number = wait_for_build_number(
        session,
        queue_url
    )

    result = monitor_build(
        session,
        build_number
    )

    if result == "SUCCESS":
        print("✅ Jenkins build completed successfully")

    else:
        print(
            f"❌ Jenkins build finished with status: {result}"
        )


if __name__ == "__main__":
    main()