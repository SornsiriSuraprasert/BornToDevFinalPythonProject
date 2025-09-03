import logging
def setup_logger():
    logging.basicConfig(
        filename="app.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)
