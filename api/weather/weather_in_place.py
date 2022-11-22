"""

@ File: weather_in_place.py
@ Date: 12.11.2022
@ Author: Ohlupin Maxim

"""
import json

from fastapi import HTTPException

from typing import Dict

from . import weather
from . import parse_response


class WeatherInPlace:
    __slots__ = ("city", "ip")

    def __init__(self, city: str | None = None, ip: str | None = None):
        self.city = city
        self.ip = ip

    async def __call__(self, *args, **kwargs) -> Dict | HTTPException:
        try:
            weather_in_city, city_name = await self._search_by()
            response_json = json.loads(weather_in_city.json())
            return parse_response(city_name, response_json)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def _search_by(self):
        if self.city is not None:
            search_city = await weather.search.by_query(self.city)
        elif self.ip is not None:
            search_city = await weather.search.by_ip(self.ip)
        else:
            raise AttributeError("Undefined Search Point")
        city_id, name = search_city[0].id, search_city[0].name
        weather_in_city = await weather.current.by_id(city_id)
        return weather_in_city, name
