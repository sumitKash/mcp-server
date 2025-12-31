from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio   # This will allow to run async call/task
import traceback # For error handling


# Creates new object called server_params
# If your server file is in diff folder then client.py , speficy that in args
server_params = StdioServerParameters(
    command="uv", # This is equivalent to MCP Host client config
    args=["run", "weather.py"],  # Optional command line arguments
)


async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool...")
                result = await session.call_tool("get_weather", arguments={"location": "DelhiNCR"})

                print("Tool result:", result)

    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
