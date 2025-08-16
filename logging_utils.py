import logging
import os


def _log_level() -> int:
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    return getattr(logging, level, logging.INFO)


def configure_logging(name: str = "app") -> logging.Logger:
    handlers = [logging.StreamHandler()]
    dest = os.getenv("LOG_DEST")
    if dest:
        handlers.append(logging.FileHandler(dest))
    logging.basicConfig(
        level=_log_level(),
        handlers=handlers,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        force=True,
    )
    return logging.getLogger(name)
