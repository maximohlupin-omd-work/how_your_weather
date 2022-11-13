"""

@ File: weather_in_place.py
@ Date: 12.11.2022
@ Author: Ohlupin Maxim

"""
import aiohttp

import urllib.parse as parse_url

from fastapi import HTTPException

from typing import Dict

from .config import WEATHER_URL
from .weather_response_parser import WeatherResponseParser


class WeatherInPlace:
    def __init__(self, city: str):
        if not isinstance(city, str):
            raise AttributeError("Arg \"city\" must be a type <str>")
        self.city = city.capitalize()

    async def __call__(self, *args, **kwargs) -> Dict | HTTPException:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    text_response = await response.text()
                    try:
                        weather_parser = WeatherResponseParser(text_response)
                        weather_dict = weather_parser.dict
                        weather_dict.update(status=200)
                        return weather_dict
                    except RuntimeError as e:
                        raise HTTPException(
                            status_code=500,
                            detail=e.args[0]
                        )
                elif response.status == 404:
                    raise HTTPException(
                        status_code=404,
                        detail="Упс, мы не смогли найти ваш город!"
                    )
                else:
                    text_response = await response.text()
                    raise HTTPException(
                        status_code=response.status,
                        detail=text_response
                    )

    @property
    def url(self):
        query_params = parse_url.urlencode(dict(
            format=4
        ))
        return WEATHER_URL + self.city + "?" + query_params
