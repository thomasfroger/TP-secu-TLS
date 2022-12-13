import socket
import string
import random


def Cesar_all():
    Messageacrypter=input("Message à chiffrer (CESAR) : ")
    msg_chiffre=random.randint(1,25) # 26=0 correspond a aucun décalage
    print("Clé de chiffrement : ",msg_chiffre)

    acrypter=Messageacrypter.upper()
    lg=len(acrypter)
    MessageCrypte=""

    for i in range(lg):
        if acrypter[i]==' ':
            MessageCrypte+=' '
        else:
            asc=ord(acrypter[i])+msg_chiffre
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

class VigenereCipher:
    """
    def encrypt(self, plain_text, key):
    def decrypt(self, cipher_text, key):
    """
    def __init__(self):
        self._plain_text = []
        self._key = ''
        self._cipher_text = []

    def encrypt(self, plain_text, key):
        """
        :param plain_text: plain text to be encrypted (str)
        :param key: key to encrypt plain text (str)
        :return: encrypted text (str)
        """
        index = 0
        self._cipher_text = ""
        self._plain_text = plain_text.lower()
        self._key = key.lower()
        for c in self._plain_text:
            if c in string.ascii_lowercase:
                off = ord(self._key[index]) - ord('a')
                encrypt_num = (ord(c) - ord('a') + off) % 26
                encrypt = chr(encrypt_num + ord('a'))
                self._cipher_text += encrypt
                index = (index + 1) % len(self._key)
            else:
                self._cipher_text += c
        return self._cipher_text

    def decrypt(self, cipher_text, key):
        """
        :param cipher_text: cipher text to be decrypted (str)
        :param key: key to decrypt cipher text (str)
        :return: decrypted text (str)
        """
        index = 0
        self._plain_text = ""
        self._cipher_text = cipher_text.lower()
        self._key = key.lower()
        for c in self._cipher_text:
            if c in string.ascii_lowercase:
                off = ord(self._key[index]) - ord('a')
                positive_off = 26 - off
                decrypt = chr((ord(c) - ord('a') + positive_off) % 26 + ord('a'))
                self._plain_text += decrypt
                index = (index + 1) % len(self._key)
            else:
                self._plain_text += c
        return self._plain_text

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


    menu_interactif="""
Proposer la méthode de chiffrement au serveur :

    cesar : Utilisation de méthode Cesar
    rot13 : Utilisation de méthode ROT 13
    vigenere : Utilisation de méthode Vigenere
    quit : Exit menu
    """
    conn.send(menu_interactif.encode())  # send data to the client
    print("[INFO] Menu envoyé au client")


    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        #print("from connected user: " + str(data))
        if data=="cesar":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            msg_chiffre=Cesar_all()
            print(msg_chiffre)
            conn.send(msg_chiffre.encode())  # send data to the client
            print("[SUCCESS] Message chiffré envoyé au client.")
            print()
        elif data=="rot13":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            msg_chiffre=RoT_13()
            print(msg_chiffre)
            conn.send(msg_chiffre.encode())  # send data to the client
            print("[SUCCESS] Message chiffré envoyé au client.")
        elif data=="vigenere":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            msg=input("Message à chiffrer (Vigenere) : ")
            obj = VigenereCipher()
            msg_chiffre=obj.encrypt(msg, 'abcdef') # returns s ek nilmsbov
            print(msg_chiffre)
            conn.send(msg_chiffre.encode())  # send data to the client
            print("[SUCCESS] Message chiffré envoyé au client.")
        else:
            print("[ERROR] Impossible de trouver cette réponse")


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()