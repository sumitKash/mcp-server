from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location: str) -> str:
      """"
          gets the weather given a location
          ARGS:
              locations: location can be city, state, street etc.
        """  
      return "weather is sunny and pleasant"  

if __name__ == "__main__":
      mcp.run()