import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ('127.0.0.1', 8000)
server_socket.bind((address[0], address[1]))
server_socket.listen()

try:
    # while True:
        connection, client_address = server_socket.accept()
        print("A New Connection!")

        buffer = b''
        while buffer[-2:] != '\r\n':
            data = connection.recv(2)
            if not data:
                break

            buffer += data
        print(f"Complete Data is {buffer}")
        connection.sendall(buffer)
finally:
    server_socket.close()
