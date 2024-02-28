import socket
import time
import math
import re
import base64
import zlib


HOST = 'challenge01.root-me.org'  # Hôte
PORT = 52022  # Port

def decode_answer(d):
    data = d.split('\n')
    line = data[6]
    chaine = line.split('\'')
    text = chaine[1]
    return decode_zlib_base64(text)

def decode_zlib_base64(texte_encodé):
    # Décodez la chaîne encodée en base64
    donnees_encodées = base64.b64decode(texte_encodé)

    # Décompressez les données avec zlib
    donnees_décompressées = zlib.decompress(donnees_encodées)

    # Retourne les données décompressées sous forme de chaîne de caractères
    return donnees_décompressées.decode('utf-8')


def decode_answer2(line):
    b64text = line.split('\'')
    b64text = b64text[1]
    
    return decode_zlib_base64(b64text)

def main():
    try:
        # Connexion au serveur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        # Réception du message du serveur
        data = s.recv(1024).decode()
        print(data)
        
        res = decode_answer(data) + '\n'
        # Envoi de la réponse au serveur
        s.send(str(res).encode())

        time.sleep(1)
        answer = s.recv(1024).decode()
        while(True):
            res = decode_answer2(answer) + '\n'
            
            s.send(str(res).encode())
            time.sleep(1)
            answer = s.recv(1024).decode()
            print(answer)
            
        
        s.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
