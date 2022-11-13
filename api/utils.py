"""

@ File: utils.py
@ Date: 13.11.2022
@ Author: Ohlupin Maxim

"""
from fastapi import Request


def get_remote_addr(request: Request) -> str:
    headers = request.headers
    x_real_ip = headers.get("x-real-ip")
    if x_real_ip is not None:
        return x_real_ip
    x_forwarded_for = headers.get("x-forwarded-for")
    if x_forwarded_for is not None:
        return x_forwarded_for
    return request.client.host
