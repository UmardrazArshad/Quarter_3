import os 

from agents import Runner,Agent, AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,RunConfig
from dotenv import load_dotenv
load_dotenv()
import chainlit as cl

#provider
provider = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

#model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client=provider
)

#agent
Agent1 = Agent(
    name = "Agent1",
    instructions = "Ypu are a helpfull assistant to assist our queries",
    model = model
)

# #config

# response = Runner.run_sync(
#     starting_agent = Agent1,
#     input = "What is the capital of Pakistan.",
# )

@cl.on_message
async def main(message: cl.Message):
    ai_response = await Runner.run(
        starting_agent = Agent1,
        input = message.content,
    )

    await cl.Message(
        content=ai_response.final_output
    ).send()