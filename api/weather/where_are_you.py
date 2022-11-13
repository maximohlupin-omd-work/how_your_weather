"""

@ File: where_are_you.py
@ Date: 11.11.2022
@ Author: Ohlupin Maxim

"""
import aiohttp

from fastapi import HTTPException

from . import config


class WhereAreYou:
    __slots__ = ("ip",)

    def __init__(self, ip_address: str):
        self.ip = ip_address

    @property
    def url(self) -> str:
        return config.WHERE_API + self.ip

    async def __call__(self, *args, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                json_response = await response.json()
                if response.status == 200:
                    if json_response["success"]:
                        return json_response["city"]
                    else:
                        raise HTTPException(
                            status_code=404,
                            detail=json_response["message"]
                        )
                else:
                    raise HTTPException(
                        status_code=response.status,
                        detail=json_response
                    )
