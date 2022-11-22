"""

@ File: gismeteo.py
@ Date: 22.11.2022
@ Author: Ohlupin Maxim

"""
import typing

from aiopygismeteo import Gismeteo

from . import config
from . import const

weather = Gismeteo()


def find_gif_desc(desc: str) -> str:
    for name, value in const.DESC_MAP.items():
        if sum(map(desc.__contains__, value)) > 0:
            return config.GIF[name]
    return "https://i.gifer.com/7H9D.gif"


def parse_response(city_name, response_json: typing.Dict):
    gif_link = find_gif_desc(response_json["description"]["full"])
    return dict(
        city=city_name,
        temperature=response_json["temperature"]["air"]["c"],
        wind="{} м\с".format(response_json["wind"]["speed"]["m_s"]),
        gif_link=gif_link
    )
