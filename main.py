from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from tools.get_date import get_current_date

provider = OpenAIProvider(
    base_url="http://localhost:11434/v1",
)

agent_model = OpenAIChatModel("qwen3:4b", provider=provider)

agent = Agent(
    model=agent_model,
    tools=[get_current_date],
    system_prompt = (
        "You have access to:\n"
        "   1. get_current_time(params: dict)\n"
        "Use this tool for date/time questions."
    )
)

import asyncio
from pydantic_ai.mcp import MCPServerStdio
async def run_async(prompt: str) -> str:
    async with agent.run_mcp_servers():
        result = await agent.run(prompt)
        return result.output

def main():
    print("Running LLM query")
    output = asyncio.run(run_async("What’s the date today?"))
    print(output)

if __name__ == "__main__":
    main()
