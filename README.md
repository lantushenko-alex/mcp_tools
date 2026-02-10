# Testing MCP tools

Basic learning tests for MCP tools and LLMs on Mac OS

tools/get_date.py 
just a basic tool to get date. Don't forget to add system prompt when use it

tools/mcp_server_time.py
MCP server. Does not require system prompt

up.sh loads model into docker llm

Issues:
1. Ollama does not work properly on Mac in docker. Need to use Docker models
2. Requires some prompt engineering in order to load MCP tool properly