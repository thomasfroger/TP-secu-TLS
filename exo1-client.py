import socket
import string
import random
from colorama import Fore, Back, Style



def client_program(cle):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = cle  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" Message pour serveur : ")  # again take input

    client_socket.close()  # close the connection



if __name__ == '__main__':


    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    data = client_socket.recv(1024).decode()  # receive response
    print(data)  # show in terminal


    message=input("Réponse : ")
    #print("Message envoyé : ",message)
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    if data=="method_accepted":
        print(Back.GREEN+"[INFO] La methode "+message+" a été acceptée par le serveur")
        data = client_socket.recv(1024).decode()
        print('Message chiffré reçu : ' + data)


    client_socket.close()  # close the connection



    #client_program(cle)