import logging
import os
import streamlit as st


def _log_level():
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    return getattr(logging, level, logging.INFO)


def _configure_logging():
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
    return logging.getLogger("app")


logger = _configure_logging()

st.set_page_config(page_title="Hello", layout="centered")
logger.info("App started")
st.write("Hello World")
