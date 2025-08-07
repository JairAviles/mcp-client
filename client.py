from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"],
)

async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("Client connected, creating session...")

                print("Session created, calling get_weather...")
                await session.initialize()

                print("Listing available tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool...")
                result = await session.call_tool("get_weather", arguments={"location": "Portland"})

                print("Tool call result:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())