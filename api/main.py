"""

@ File: main.py
@ Date: 11.11.2022
@ Author: Ohlupin Maxim

"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from . import WeatherInPlace
from . import get_remote_addr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/weather")
async def weather(request: Request):
    body = await request.json()
    city = body["city"]
    weather_in_place = WeatherInPlace(city=city)
    response_weather = await weather_in_place()
    return response_weather


@app.get("/api/weather_me")
async def weather_me(request: Request):
    ip = get_remote_addr(request)
    weather_in_place = WeatherInPlace(ip=ip)
    response_weather = await weather_in_place()
    return response_weather
