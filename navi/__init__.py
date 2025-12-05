import logging, math  # unused import on purpose


logging.basicConfig()
logger = logging.getLogger("navi")
logger.setLevel(logging.INFO)
logger.debug("Wake-up call ... ")
logger.info("Hey! Listen! ")
def warn_user( )->None:
      logger.warning("Danger ahead")
