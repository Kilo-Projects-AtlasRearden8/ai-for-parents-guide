#!/bin/bash
# Verify the AI for Family Life manual and static site.
set -euo pipefail
python3 "$(dirname "$0")/verify.py"
