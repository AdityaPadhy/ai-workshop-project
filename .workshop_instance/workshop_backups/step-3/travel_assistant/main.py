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


load_dotenv(override=True)


def main() -> None:
    # Foundry model client, built from your .env settings.
    client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=DefaultAzureCredential(),
    )

    # TODO: write TravelBuddy's system instructions. Describe a friendly travel
    # assistant that gives practical, concise trip-planning advice — local context,
    # budget awareness, and safety-minded tips.

    agent = Agent(
        client=client,
        name="travel-buddy",
        instructions="a friendly travel assistant that gives practical, concise trip-planning advice with local context, budget awareness, and safety-minded tips",
        tools=[get_weather, get_local_time, convert_currency, client.get_mcp_tool(                          # <-- add this entry
            name=os.environ["MCP_SERVER_LABEL"],
            url=os.environ["MCP_SERVER_URL"],
            approval_mode="never_require",
        ),],  # <-- add this line
        default_options={"store": False},
    )



    ResponsesHostServer(agent).run()


if __name__ == "__main__":
    main()
