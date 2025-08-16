import os
import json
import streamlit as st
import threading
from mcp_server import server as mcp_server

st.set_page_config(page_title="Stock MCP (on‑demand)", layout="centered")
st.title("Stock MCP — on‑demand client")

server_thread = None

def start_mcp_process():
    global server_thread
    if server_thread is not None:
        return server_thread
    def run_mcp_server():
        mcp_server.run()
    server_thread = threading.Thread(target=run_mcp_server)
    server_thread.start()
    st.success(f"MCP server started (pid {server_thread.ident})")
    return server_thread


if st.button("Start MCP Server"):
    try:
        proc = start_mcp_process()
        #st.success(f"MCP server started (pid {proc.ident})")
    except Exception as e:
        st.exception(e)

 # --- Simple UI ---
symbol = st.text_input("Stock symbol", value="AAPL", max_chars=10)

if st.button("Get Quote"):
    # Intentionally minimal for a clean restart. We'll wire up the stdio call next.
    st.info(
        "On‑demand request logic not implemented yet — starting from scratch as requested."
    )
    st.code(
        """
        # Pseudocode for next step:
        # - Spawn MCP process with subprocess using MCP_CMD
        # - Send a single JSON-RPC request over stdio using MCP_METHOD and {"symbol": SYMBOL}
        # - Read one response (LSP framing or NDJSON), then show it
        """,
        language="python",
    )
