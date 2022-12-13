import socket


if __name__ == '__main__':


    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    data = client_socket.recv(1024).decode()  # receive response
    print(data)  # show in terminal


    actual_method=input("Choix : ")
    print('\n')
    #print("Message envoyé : ",message)
    client_socket.send(actual_method.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('[INFO] Retour du serveur : ' + data)  # show in terminal
    if data=="method_accepted":

        print("[INFO] La methode "+actual_method+" a été acceptée par le serveur"+'\n')
        
        # Envoi du message à chiffrer
        message=input("Message à chiffrer avec "+actual_method+" : ")
        client_socket.send(message.encode())  # send message

        # Envoi de la clé de chiffrement
        message=input("Cle de chiffrement avec "+actual_method+" : ")
        client_socket.send(message.encode())  # send message

        # Reception du message déchiffré
        data = client_socket.recv(1024).decode()
        print('Message dechiffré : ' + data)


    client_socket.close()  # close the connection
