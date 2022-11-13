"""

@ File: config.py
@ Date: 12.11.2022
@ Author: Ohlupin Maxim

"""
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "settings.ini"))

WEATHER_API = config["WEATHER_API"]
WEATHER_URL = WEATHER_API["API_URL"]

WHERE_ARE_YOU = config["WHERE_ARE_YOU"]
WHERE_API = WHERE_ARE_YOU["API_URL"]
