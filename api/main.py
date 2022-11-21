"""

@ File: main.py
@ Date: 11.11.2022
@ Author: Ohlupin Maxim

"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from . import WeatherInPlace
from . import WhereAreYou
from . import get_remote_addr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/weather")
async def weather(request: Request):
    body = await request.json()
    city = body["city"]
    weather_in_place = WeatherInPlace(city=city)
    response_weather = await weather_in_place()
    return response_weather


@app.get("/weather_me")
async def weather_me(request: Request):
    ip = get_remote_addr(request)
    where_are_you = WhereAreYou(ip_address=ip)
    city = await where_are_you()
    weather_in_place = WeatherInPlace(city=city)
    response_weather = await weather_in_place()
    return response_weather


@app.get("/me_city")
async def read_root(request: Request):
    ip = get_remote_addr(request)
    where_are_you = WhereAreYou(ip_address=ip)
    city = await where_are_you()
    return dict(city=city)
