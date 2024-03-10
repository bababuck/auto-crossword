#!/bin/bash

export OPENAI_API_KEY=$(cat ~/.ssh/openai)
python3 main.py $@
