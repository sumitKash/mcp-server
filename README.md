Getting Started
This project uses uv for fast Python dependency management and virtual environments.
Follow these steps to set up and run the MCP (Modular Context Protocol) server.

Prerequisites
Python 3.8+.
Terminal access.
uv package manager
npm
claude desktop(Optional) - If you want to work with LLM host


Installation and Setup

Install uv: Follow the official guide.

Initialize Project (from project root):
uv init

Create and Activate Virtual Environment:
uv venv
source .venv/bin/activate  

Install MCP CLI:
uv add "mcp[cli]" #Quotes are needed

Running the Server
Start in dev mode (with hot-reload and logging):
mcp dev <MCP_SERVER>.py  # e.g., mcp dev screenshot.py

Additional Dependencies
Install per-server extras as needed (via uv add in the activated env):

screenshot.py: pyautogui, pyscreeze, pillow (for screen capture).
crypto.py: requests (for HTTP operations).

If import errors occur, add the missing package and rerun.

Troubleshooting
Ensure env is activated ((.venv) in prompt).
Deactivate with deactivate.


