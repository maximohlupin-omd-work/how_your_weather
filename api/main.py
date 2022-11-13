"""

@ File: main.py
@ Date: 11.11.2022
@ Author: Ohlupin Maxim

"""
from fastapi import FastAPI, Request

from . import WeatherInPlace

app = FastAPI()


@app.post("/weather")
async def weather(request: Request):
    body = await request.json()
    city = body["city"]
    weather_in_place = WeatherInPlace(city=city)
    response_weather = await weather_in_place()
    return response_weather


@app.get("/weather_me")
async def weather_me(request: Request):
    body = await request.json()
    city = body["city"]
    weather_in_place = WeatherInPlace(city=city)
    response_weather = await weather_in_place()
    return response_weather


@app.get("/me_city")
def read_root(request: Request):
    print(request.client)
    return request.headers
