from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import asyncio
app = FastAPI()
class reg_person(BaseModel):
    name: str
    email: str
    password: str
    replay_password: str
class login_person(BaseModel):
    name: str
    password: str
@app.post("/registration")
def prin(mass:reg_person):
    return {"Имя пользователя":mass.name,"Емейл пользователя":mass.email}
@app.get("/messange")
def LOOK_messange():
    return 
@app.post("/login")
def login():
    return
@app.post("/messages")
def messages():
    return
