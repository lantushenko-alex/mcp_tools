from pydantic_ai.mcp import MCPServerStdio

time_server = MCPServerStdio(
    "python",
    args=["-m", "mcp_server_time", "--local-timezone=America/New_York"],
)
