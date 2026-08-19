# travel_assistant/main.py — Python entry point that hosts TravelBuddy: it creates
# the Foundry model client, defines the agent, and starts the Responses server.
# Complete the one TODO inside main() below.
import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from tools import convert_currency, get_local_time, get_weather
from agent_framework_foundry_hosting import FoundryToolbox, ResponsesHostServer
from agent_framework.azure import AzureAISearchContextProvider  # NEW
import subprocess    # NEW
import sys           # NEW
from pathlib import Path  # NEW
from typing import Any    # NEW
import asyncio
import io
import shutil
import tempfile
import zipfile
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import DefaultAzureCredential as AsyncDefaultAzureCredential
from agent_framework_foundry_hosting import ResponsesHostServer

from coordinator import build_travel_coordinator

def main() -> None:
    # The Coordinator + specialists group chat is exposed as a single agent, so the
    # rest of the hosting stack is unchanged from earlier steps.
    agent = build_travel_coordinator()
    ResponsesHostServer(agent).run()


if __name__ == "__main__":
    main()
