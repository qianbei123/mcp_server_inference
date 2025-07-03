#!/bin/bash
source /app/.venv/bin/activate
fastmcp run molecule_search_service.py --transport sse --host 0.0.0.0 --port 5005 2>&1 | tee /app/molecule_search_service.log 