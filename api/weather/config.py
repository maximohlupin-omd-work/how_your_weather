"""

@ File: config.py
@ Date: 12.11.2022
@ Author: Ohlupin Maxim

"""
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "settings.ini"))

WHERE_ARE_YOU = config["WHERE_ARE_YOU"]
WHERE_API = WHERE_ARE_YOU["API_URL"]

GIF = config["GIF"]
RAIN = GIF["RAIN"]
SUN = GIF["SUN"]
CLOUDY = GIF["CLOUDY"]
SNOW = GIF["SNOW"]
