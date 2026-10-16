# 1. List containers managed by our python automation
# 2. Identify stopped containers
# 3. Display container status and recent logs
# 4. Offer an optional cleanup mode
# 5. log operations and errors

import argparse
import logging
import docker

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("docker_monitor.log")
    ]
)

logger = logging.getLogger(__name__)

# LABEL = "managed-by=python-demo"


def connect_to_docker():
    client = docker.from_env()
    client.ping()
    return client


def monitor_containers(client):
    containers = client.containers.list(
        all=True,
        # filters={"label": LABEL}
    )

    if not containers:
        logger.info("No managed containers found.")
        return []

    for container in containers:
        try:
            container.reload()
            logger.info(
                "Name=%s ID=%s Status=%s",
                container.name,
                container.short_id,
                container.status
            )

            if container.status == "exited":
                logger.warning(
                    "Stopped container detected: %s",
                    container.name
                )

                logs = container.logs(tail=5)
                logger.info(
                    "Recent logs for %s:\n%s",
                    container.name,
                    logs.decode("utf-8", errors="replace")
                )

        except docker.errors.NotFound:
            logger.warning(
                "Container disappeared during inspection."
            )
        except docker.errors.APIError:
            logger.exception(
                "Docker API error inspecting %s",
                container.name
            )

    return containers


def cleanup_stopped(containers):
    for container in containers:
        try:
            container.reload()

            if container.status == "exited":
                logger.warning(
                    "Removing stopped container: %s",
                    container.name
                )
                container.remove()

        except docker.errors.NotFound:
            logger.info("Container already removed.")
        except docker.errors.APIError:
            logger.exception(
                "Failed to remove %s",
                container.name
            )


def main():
    parser = argparse.ArgumentParser(
        description="Monitor Python-managed Docker containers"
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Remove stopped containers carrying the managed label"
    )
    args = parser.parse_args()

    try:
        client = connect_to_docker()
        logger.info("Connected to Docker Engine.")

        containers = monitor_containers(client)

        if args.cleanup:
            cleanup_stopped(containers)
        else:
            logger.info(
                "Read-only mode. Use --cleanup to remove stopped "
                "managed containers."
            )

        client.close()

    except docker.errors.DockerException:
        logger.exception("Could not connect to Docker or complete operation.")


if __name__ == "__main__":
    main()
