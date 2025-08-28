import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

load_dotenv()


app = FastAPI()


templates = Jinja2Templates(directory="templates")


def send_message(message: str):
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("BOT_CHAT")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        "chat_id": chat_id,
        "text": message
    }
    
    response = requests.post(url, data=data)
    
    print(response.content)
    
    if not response.ok:
        return False
    
    return True



class Message(BaseModel):
    message: str
@app.post("/message")
async def web_message(data: Message):
    
    send_message(f"🚨 NEW MESSAGE\n\n👉 {data.message}")
    
    return {"detail": "is worked!"}



@app.get("/")
async def client_send(request: Request):

    return templates.TemplateResponse(request=request, name="index.html")



if __name__ == "__main__":
    print("hello world")