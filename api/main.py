"""

@ File: main.py
@ Date: 11.11.2022
@ Author: Ohlupin Maxim

"""
from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    print(request.client)
    return request.headers


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
