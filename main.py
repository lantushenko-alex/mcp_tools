from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from tools.mcp_server_calc import calc_server

import asyncio

from tools.mcp_server_time import time_server

provider = OpenAIProvider(
    base_url="http://localhost:12434/engines/v1",
)

agent_model = OpenAIChatModel("ai/qwen3:0.6B-Q4_0", provider=provider)

agent = Agent(
    model=agent_model,
    tools=[],
    mcp_servers=[time_server, calc_server]
)


async def run_async(prompt: str) -> str:
    async with agent:
        return (await agent.run(prompt)).output


def main():
    print("Running LLM query")
    output = asyncio.run(run_async("What is (12 + 8) * 3"))
    print(output)


if __name__ == "__main__":
    main()
