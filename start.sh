#!/usr/bin/env bash
set -euo pipefail

if [ -d "venv" ]; then
  source venv/bin/activate
fi

echo "Starting ping monitor..."
sleep 2
python3 sc.py