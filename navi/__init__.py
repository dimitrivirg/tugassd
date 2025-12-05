import logging

logging.basicConfig()
logger = logging.getLogger("navi")
logger.setLevel(logging.INFO)


logger.debug("Wake-up call ... ")
logger.info("Hey! Listen! ")


def warn_user() -> None:
    """Emit a warning message using the navi logger."""
    logger.warning("Danger ahead")
