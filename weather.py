from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

# Docstring in below fucntion is important bz MCP client is actually able to grab the tool
# and then pass it to the LLM 
 
@mcp.tool() #decorator, elevated the below function to status of a tool
def get_weather(location: str) -> str:
      """"
          gets the weather given a location
          ARGS:
              locations: location can be city, state, street etc.
        """  
      return "weather is sunny and pleasant"  

if __name__ == "__main__":
      mcp.run()
