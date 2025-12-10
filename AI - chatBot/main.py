from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

# Tools - yaha pe predifined outputs ko set karskte hai
@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"
    
@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today"

def main():
    # Model define hoga temp 0 ke saath so that randomness will ben null.
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest", # Latest model will be used 
        temperature=0,
        api_key=os.getenv("GOOGLE_API_KEY")  # env se key use karke api model fetch hoga
    )
    
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools) # Agent me predefined params pass karskte hai with this
    
    print("Welcome! I'm your AI assistant (Gemini). Type 'quit' to exit.") # starter mssgs
    print("You can ask me to perform calculations or chat with me.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "quit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [("user", user_input)]}  
        ):
            messages = chunk.get("messages", []) or chunk.get("agent", {}).get("messages", [])
            for message in messages:
                print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
 
 # And VOILA we have created a personal ASSISTANT who calls me BOSS :)