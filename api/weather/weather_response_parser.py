"""

@ File: weather_response_parser.py
@ Date: 12.11.2022
@ Author: Ohlupin Maxim

"""
from typing import List


class WeatherResponseParser:
    __slots__ = ("text",)

    def __init__(self, response_text: str):
        self.text = response_text

    def parse(self) -> List:
        text = self.text.replace("\n", "").replace("\t", "_").replace(" ", "_")
        text = text.split("_")
        weather_list = []
        for elem in text:
            if ":" in elem:
                weather_list.insert(0, elem[:-1])
            elif "C" in elem:
                weather_list.insert(1, elem[2:])
            elif "km/h" in elem:
                weather_list.insert(2, elem[3:])
            else:
                continue
        return weather_list

    @property
    def dict(self):
        weather = self.parse()
        if len(weather) == 3:
            return dict(
                city=weather[0],
                temperature=weather[1],
                wind=weather[2],
            )
        raise RuntimeError("Ошибка ответа от сервиса погоды!")
