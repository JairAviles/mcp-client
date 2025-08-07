from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a specified location.
    Args:
        location (str): The name of the location to get the weather for.
    """
    # Placeholder implementation
    return "The current weather in {location} is cloudy and gloomy."

if __name__ == "__main__":
    mcp.run()