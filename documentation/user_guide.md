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

## FastMCP Server
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python mcp_server.py`
3. The server provides a `get_stock_quote` tool that fetches prices using the free Alpha Vantage demo API.
