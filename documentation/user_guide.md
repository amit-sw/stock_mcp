# User Guide

## Starting the App
1. Install dependencies: `pip install -r requirements.txt`
2. Start the app: `streamlit run app.py`
3. Open the URL shown in the terminal. You should see: `Hello World`.

## Configuration
- Optional environment variables:
  - `LOG_LEVEL`: `DEBUG` | `INFO` | `WARN` | `ERROR` (default `INFO`)
  - `LOG_DEST`: file path to also write logs (in addition to console)

## Troubleshooting
- If the app doesn't start, verify Python version (3.9+) and Streamlit installation.
- Check terminal output for errors and logs.
