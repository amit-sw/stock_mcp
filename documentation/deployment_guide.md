# Deployment Guide

## Prerequisites
- Python 3.9+
- pip

## Local Run
- Install dependencies: `pip install -r requirements.txt`
- Start the app: `streamlit run app.py`

## Configuration (Environment Variables)
- `LOG_LEVEL` (optional): `DEBUG` | `INFO` | `WARN` | `ERROR` (default: `INFO`)
- `LOG_DEST` (optional): file path to also write logs (in addition to console)

## Notes
- `.streamlit/secrets.toml` is ignored by git. Create it locally if needed for future features; do not commit it.

## Verification
- After starting, the app should display: `Hello World`.
