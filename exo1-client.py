import socket
import string
from random import *



def Cesar_all():
    Messageacrypter=input("Message à chiffrer (CESAR) : ")
    cle=randint(1,25) # 26=0 correspond a aucun décalage
    print("Clé de chiffrement : ",cle)

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


def  RoT_13():

    alphabet_maj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random_list=random.sample(alphabet_maj, len(alphabet_maj))
    list_maj = ''.join(random_list)
    print(list_maj)
    alphabet_min=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random_list=random.sample(alphabet_min, len(alphabet_min))
    list_min = ''.join(random_list)
    print(list_min)
    all_alphabet=alphabet_maj+alphabet_min
    print(all_alphabet)


    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    txt = input("Message à chiffrer (ROT13) : ")
    return (txt.translate(rot13trans))

def simple_transposition():
    pass


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
Choix de la méthode de chiffrement :

    1.Cesar
    2.ROT13
    3.Inactif
    4.Exit/Quit
    """)
    response=input("Numéro de choix :") 
    if response=="1": 
        cle=Cesar_all() 
    elif response=="2":
        cle=RoT_13()
    elif response=="3":
        print("\n ") 
    elif response=="4":
        print("\n ") 
    elif response !="":
        print("\n Choix invalide. Réessayez") 
    
    client_program(cle)