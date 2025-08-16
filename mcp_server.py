import os
import requests
from fastmcp import FastMCP
import streamlit as st

from logging_utils import configure_logging

logger = configure_logging("mcp")
server = FastMCP("Stock MCP Server")

API_URL = "https://www.alphavantage.co/query"
#API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "demo")
API_KEY=st.secrets["ALPHAVANTAGE_API_KEY"]

@server.tool()
def get_stock_quote(symbol: str) -> dict:
    """Fetch the latest stock quote for ``symbol`` using the Alpha Vantage demo API."""
    params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": API_KEY}
    logger.info("Fetching quote for %s", symbol)
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json().get("Global Quote", {})
    if not data:
        return {"symbol": symbol.upper(), "price": None}
    return {
        "symbol": data.get("01. symbol", symbol.upper()),
        "price": float(data.get("05. price", "0") or 0.0),
        "change_percent": data.get("10. change percent"),
    }


if __name__ == "__main__":
    server.run()
