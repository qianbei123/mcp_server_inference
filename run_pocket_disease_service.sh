#!/bin/bash
source /app/.venv/bin/activate
fastmcp run Pocket_Molecule_Disease_Service.py --transport sse --host 0.0.0.0 --port 5006 2>&1 | tee /app/pocket_disease_service.log 