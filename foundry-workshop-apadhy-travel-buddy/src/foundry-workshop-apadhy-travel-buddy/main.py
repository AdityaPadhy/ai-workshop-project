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


load_dotenv(override=True)


def main() -> None:
    # Foundry model client, built from your .env settings.

    # TODO: write TravelBuddy's system instructions. Describe a friendly travel
    # assistant that gives practical, concise trip-planning advice — local context,
    # budget awareness, and safety-minded tips.


    credential = DefaultAzureCredential()

    client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=credential,                # <-- reuse the same credential
    )

    toolbox = FoundryToolbox(credential)

    agent = Agent(
        client=client,
        name="travel-buddy",
        instructions="Use the Foundry Toolbox for flight search (when the traveler gives no "
            "departure date, call get_local_time and use the date part of its "
            "iso_time as today's date), for web search of current "
            "travel advisories and events, and for Code Interpreter to analyze an "
            "uploaded itinerary.csv (budget totals, currency conversion, charts).",
        tools=[get_weather, get_local_time, convert_currency, toolbox],  # <-- add this line
        default_options={"store": False},
    )



    ResponsesHostServer(agent).run()


if __name__ == "__main__":
    main()
