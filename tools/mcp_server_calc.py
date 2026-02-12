from mcp.server.fastmcp import FastMCP
from pydantic_ai.mcp import MCPServerStdio

mcp = FastMCP("Calculator")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b and return the result. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

calc_server = MCPServerStdio(
    "python",
    args=["tools/mcp_server_calc.py"],
)

if __name__ == "__main__":
    mcp.run()