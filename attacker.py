import socket
import logging

host = '192.168.1.198' # The server's local IP address here (replace with 127.0.0.1 for localhost)
port = 55555

# Configurating for logging
logging.basicConfig(filename="logs.log", level=logging.DEBUG)

# Starting Listening Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

# Accepting the connection by the client
conn, address = server.accept()

print("Connected by:", conn)

# Infinite loop to always be listening
while True:
    # Trying to receive data
    data = conn.recv(1024)

    # Decoding and printing data
    print("From client:", data.decode("utf-8"))
    # Logging data
    logging.info(data.decode("utf-8"))