import socket
import string
import random

def Cesar_all():
    Messageacrypter=input("Message à chiffrer (CESAR) : ")
    cle=random.randint(1,25) # 26=0 correspond a aucun décalage
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
    alphabet_min=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random_list=random.sample(alphabet_min, len(alphabet_min))
    list_min = ''.join(random_list)
    all_alphabet=list_maj+list_min
    print("Clé de chiffrement : ",all_alphabet)


    rot13trans = str.maketrans(all_alphabet, 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    txt = input("Message à chiffrer (ROT13) : ")
    return (txt.translate(rot13trans))

def simple_transposition():
    pass



def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        if data=="cesar":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            Cesar_all()
        elif data=="rot13":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            cle=RoT_13()
            print(cle)
            conn.send(cle.encode())  # send data to the client


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()