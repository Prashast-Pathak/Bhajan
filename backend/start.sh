#!/bin/bash

# Master Sheet Webhook (Using 1 sheet to track all 6 pillars easily!)
export GSHEET_WEBHOOK_BHAJANS="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"
export GSHEET_WEBHOOK_SHLOKAS="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"
export GSHEET_WEBHOOK_PRAYERS="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"
export GSHEET_WEBHOOK_GITA="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"
export GSHEET_WEBHOOK_UPANISHADS="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"
export GSHEET_WEBHOOK_WISDOM="https://script.google.com/macros/s/AKfycbyUfnAOMp9CksGdArfVGGw5eRa9u9W99X3lwTBgC9cBI3zmhixJLW53ILs2RlLMjOXS/exec"

echo "Starting the Bhajan Content Brain 🧠"
echo "Sending all spreadsheet updates to your master tracking sheet..."

# Ensure the virtual environment is set up and activated
if [ ! -d ".venv" ]; then
    echo "First time setup: Installing the required tools..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# Start the Backend Server!
uvicorn app:app --host 127.0.0.1 --port 8090 --reload
