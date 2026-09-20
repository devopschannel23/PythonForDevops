import logging
#logger -> handler -> formatter -> output
logger=logging.getLogger("deployment")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("deployment.log")

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Deployment started")
logger.warning("Deployment is taking much time")
logger.error("Deployment failed!")

