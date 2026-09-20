import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
try:
    result1 = 10/0
# except Exception as e:
#     logging.error("You cannot divide any integer by 0: %s", e)
except Exception:
    logging.exception("Division by 0 Exception")

