import os 

from agents import Runner,Agent, AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,RunConfig
from dotenv import load_dotenv
load_dotenv()

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

#config

response = Runner.run_sync(
    starting_agent = Agent1,
    input = "What is the capital of India.",
)

print (response.final_output)

def main():
    history= []

    while True:
        user_input = input("Enter your message. Type 'exit' to quit: ")
    
        if user_input.lower() == 'exit':
            break
    
        history.append({"role": "user", "content": user_input})
    
        response = Runner.run_sync(
            starting_agent = Agent1,
            input = history,
        )
    
        history.append({"role": "assistant", "content": response.final_output})

        print ("Assistant : " , response.final_output)

main()