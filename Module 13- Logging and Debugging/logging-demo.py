import logging

logging.basicConfig(filename="logs.log",
                    level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Starting deployment")
logging.debug("Debug mode enabled")
logging.disable("Something is wrong, DB is un-reachable!")

