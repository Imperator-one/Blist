from fastapi import FastAPI
import asyncio
app = FastAPI()
@app.post("/Register/")
async def pri(mass = {}):
    return mass
@app.get("/Register/")
async def exi():
    return
print(asyncio.run(pri()))