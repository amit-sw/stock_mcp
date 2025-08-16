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

def get_quote(symbol: str):
    import asyncio

    async def _run():
        tools=await mcp_server.get_tools()
        tool=tools.get("get_stock_quote")
        if not tool:
            raise Exception("get_stock_quote tool not found")
        return await tool.run({"symbol": symbol})

    return asyncio.run(_run())


if st.button("Start MCP Server"):
    try:
        proc = start_mcp_process()
        #st.success(f"MCP server started (pid {proc.ident})")
    except Exception as e:
        st.exception(e)

# Button to list available MCP server commands
if st.button("List MCP Commands"):
    try:
        import asyncio
        tools = asyncio.run(mcp_server.get_tools())
        if tools:
            st.write("Available commands:")
            for name in tools.keys():
                st.write(f"- {name}")
        else:
            st.info("No commands available.")
    except Exception as e:
        st.exception(e)

 # --- Simple UI ---
symbol = st.text_input("Stock symbol", value="AAPL", max_chars=10)

if st.button("Get Quote"):
    try:
        quote = get_quote(symbol)
        st.write(quote)
    except Exception as e:
        st.exception(e)
