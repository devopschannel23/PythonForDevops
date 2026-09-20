import logging
import subprocess

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Checking Kubernetes Nodes...")
try:
    result1= subprocess.run(["kubectl", "get", "nodes"], capture_output=True, text=True, check=True)
    logging.info("Kubectl command executes successfully")
    logging.info("Output:\n%s", result1.stdout)
except subprocess.CalledProcessError:
    logging.exception("Failed to execute kubectl command!")