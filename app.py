import streamlit as st

from logging_utils import configure_logging


logger = configure_logging()

st.set_page_config(page_title="Hello", layout="centered")
logger.info("App started")
st.write("Hello World")
