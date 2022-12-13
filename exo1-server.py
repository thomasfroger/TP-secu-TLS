import socket
import random
from itertools import product as col



def Cesar_chiffrer():
    Messageacrypter=input("Message à chiffrer (CESAR) : ")
    cle_cesar=random.randint(1,25) # 26=0 correspond a aucun décalage
    print("Clé de chiffrement : ",cle_cesar)

    acrypter=Messageacrypter.upper()
    lg=len(acrypter)
    message_chiffre=""

    for i in range(lg):
        if acrypter[i]==' ':
            message_chiffre+=' '
        else:
            asc=ord(acrypter[i])+cle_cesar
            message_chiffre+=chr(asc+26*((asc<65)-(asc>90)))
    
    result=message_chiffre+"-"+str(cle_cesar)
    return result

def Cesar_dechiffrer(phrase_cesar,cle_cesar):
    
    MessageCrypte=phrase_cesar
    lg=len(MessageCrypte)
    MessageClair=""
    cle=int(cle_cesar) # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)

    for i in range(lg):
        if MessageCrypte[i]==' ':
            MessageClair+=' '
        else:
            asc=ord(MessageCrypte[i])-cle
            MessageClair+=chr(asc+26*((asc<65)-(asc>90)))
    
    return MessageClair

def RoT_13_chiffrer():

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

def RoT_13_dechiffrer(phrase_rot13,cle_rot13):
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        cle_rot13)
    return (phrase_rot13.translate(rot13))

def Vigenere_dechiffrer(x,key):
    lst_final = []
    encrypt = False
    code = list(x)
    j = 0
	
    for i,char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i+j)%len(key)]
            if encrypt:
                lst_final.append((ord(x[i]) + ord(code[i]) - 65 * 2) % 26)
            else:
                lst_final.append((ord(x[i]) - ord(code[i])) % 26)
        else:
            lst_final.append(ord(char))
            j -=1

    for i,char in enumerate(code):
        if char.isalpha():
            lst_final[i] = chr(lst_final[i] + 65)
        else:
            lst_final[i] = chr(lst_final[i])
			
    return ''.join(lst_final)


if __name__ == '__main__':

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
        
        # Reception de la methode choisie
        data = conn.recv(1024).decode()
        print("[INFO] Choix du client : " + str(data))


        if data=="cesar":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            phrase = conn.recv(1024).decode()
            print("Phrase du client : "+phrase)
            cle_cesar = conn.recv(1024).decode()
            print("Cle du client : "+cle_cesar)

            result=Cesar_dechiffrer(phrase,cle_cesar)
            print("La phrase déchiffrer par le serveur : ",result)
            conn.send(result.encode())  # send data to the client


        elif data=="rot13":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            phrase_rot13 = conn.recv(1024).decode()
            print("Phrase du client : "+phrase_rot13)
            cle_rot13 = conn.recv(1024).decode()
            print("Cle du client : "+cle_rot13)

            result=RoT_13_dechiffrer(phrase_rot13,cle_rot13)
            print("La phrase déchiffrer par le serveur : ",result)
            conn.send(result.encode())  # send data to the client


        elif data=="vigenere":
            data = "method_accepted"
            conn.send(data.encode())  # send data to the client
            phrase_vigenere = conn.recv(1024).decode()
            print("Phrase du client : "+phrase_vigenere)
            cle_vigenere = conn.recv(1024).decode()
            print("Cle du client : "+cle_vigenere)
            x = phrase_vigenere.upper()
            key = cle_vigenere.upper()

            
            result=Vigenere_dechiffrer(x,key)
            print("La phrase déchiffrer par le serveur : ",result)
            conn.send(result.encode())  # send data to the client

        elif data=="exit":
            conn.close()
        else:
            print("[ERROR] Impossible de trouver cette réponse")
            conn.close()
    
    conn.close() # close the connection