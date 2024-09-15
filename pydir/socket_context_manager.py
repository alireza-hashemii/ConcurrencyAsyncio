import asyncio
from typing import Optional, Type
import socket

class SocketConnected():
    def __init__(self, server_socket) -> None:
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        loop = asyncio.get_event_loop()
        connection , addresss = await loop.sock_accept(self._server_socket)
        print("Got a qualified connection!".title())
        self._connection = connection
        return self._connection
    
    async def __aexit__(self,exc_type: Optional[Type[BaseException]],
                exc_val: Optional[BaseException],x):
        print('connection is getting closed.')
        self._connection.close()
        print("connection got closed".title())


async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    async with SocketConnected(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)

asyncio.run(main())


import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status
    

async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.01)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://example.com')