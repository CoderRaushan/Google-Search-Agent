from fastapi import FastAPI
from pydantic import BaseModel
from google_search_agent import agent

app=FastAPI()

class ChatRequest(BaseModel):
    message:str


@app.post("/chat")
async def chat(request:ChatRequest):
    response=await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request.message
            }
        ]
    },
       config={
            "configurable": {
                "thread_id": "user-1"
            }
        }
    )

    return {
        "response": response["messages"][-1].content
    }