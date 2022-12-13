import socket

def Cesar_all():
    Messageacrypter=input("Message à chiffrer (CESAR) : ")
    cle=24 # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)

    acrypter=Messageacrypter.upper()
    lg=len(acrypter)
    MessageCrypte=""

    for i in range(lg):
        if acrypter[i]==' ':
            MessageCrypte+=' '
        else:
            asc=ord(acrypter[i])+cle
            MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))
    return MessageCrypte




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
    cle=Cesar_all()
    client_program(cle)