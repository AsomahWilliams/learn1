from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
async def read_root():
    return{"message":"welcome to De Don Api"}


@app.get("/greet/")
async def greet_name(name:str) -> dict:
    return{"message:"}