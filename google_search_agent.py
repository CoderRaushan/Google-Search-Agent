from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper 
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.agents import create_agent 
from langgraph.checkpoint.memory import InMemorySaver  

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

search=GoogleSerperAPIWrapper()

agent = create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="you are an agent and can search for any question on google",
    checkpointer=InMemorySaver(),
)
