import asyncio
from typing import Optional, Type, TracebackType
import socket

class ConnectedSocket:
    def __init__(self, server_socket) -> None:
        self._connection = None
        self._server_socket = server_socket

    
    async def __aenter__(self):
        msg = "Trying to get a connection..."
        for i in msg:
            await asyncio.sleep(1)
            print(f" \r {i}")

        loop = asyncio.get_event_loop()
        connection , address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print("I got a connection!")
        return self._connection
    

    async def __aexit__(self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]): 
        
        print('Exiting context manager')
        self._connection.close()
        print('Closed connection')



async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection: 
        data = await loop.sock_recv(connection, 1024)
        print(data) 
