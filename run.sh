#!/bin/bash
source /app/.venv/bin/activate
fastmcp run main.py --transport sse --port 5003 2>&1 | tee /app/server.log