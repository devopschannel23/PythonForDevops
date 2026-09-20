import logging
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_pods(namespace):

    command = [
        "kubectl",
        "get",
        "pods",
        "-n",
        namespace
    ]

    logging.info(
        "Executing command: %s",
        " ".join(command)
    )
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout


def main():

    namespace = "production"

    logging.info("Checking Kubernetes pods")

    pods = get_pods(namespace)

    print(pods)


if __name__ == "__main__":
    main()