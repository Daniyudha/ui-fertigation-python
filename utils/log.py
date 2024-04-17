import logging

def log() -> logging:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        filename="log/log.log"
    )
    return logging
