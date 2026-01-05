from mcp.server.fastmcp import FastMCP
#Since the program is going to return image
from mcp.server.fastmcp.utilities.types import Image

#Needed to take screenshots, make sure you have this library, else install it
import pyautogui
import io

#Create server
mcp = FastMCP("Desktop Screenshot")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Captures a screenshot of the current screen (or active window) and returns it as a PIL Image object for easy handling.
    
    Invoke this tool whenever the user requests a screenshot to capture their on-screen activity, such as for 
    troubleshooting, verifying states, or providing visual context in workflows. It processes the capture in memory 
    for speed and cleanliness, avoiding temporary files.
    """
    
#By using buffer object we can store image data without disk I/O, Enable easy loading into an image object
    buffer = io.BytesIO()

    # if the file exceeds ~1MB, it will be rejected by Claude
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getvalue(), format="jpeg")

if __name__ == "__main__":
    mcp.run()
