import socket
import string
import random




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


    print ("""
Proposer la méthode de chiffrement :

    1.Cesar
    2.ROT13
    3.Vigenere
    4.Simple Transposition
    5.Exit/Quit
    """)
    response=input("Numéro de choix :") 
    if response=="1": 
        print("--- Vous avez proposé la méthode Cesar ---")
        message="cesar"
        #cle=Cesar_all() 
    elif response=="2":
        print("--- Vous avez proposé la méthode ROT13 ---")
        message="rot13"
        #cle=RoT_13()
    elif response=="3":
        message="vigenere"
    elif response=="4":
        print("\n ") 
    elif response !="":
        print("\n Choix invalide. Réessayez") 
    


    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    print("Message envoyé : ",message)
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    if data=="method_accepted":
        print("La methode "+message+" a été accepté par le serveur")
        data = client_socket.recv(1024).decode()
        print('Message chiffré reçu : ' + data)


    client_socket.close()  # close the connection



    #client_program(cle)