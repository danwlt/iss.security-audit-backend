#!/bin/bash

set -e
python mongo_startup.py
uvicorn main:app --host 0.0.0.0 --port 80