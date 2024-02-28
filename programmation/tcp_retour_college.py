import socket
import time
import math
import re

HOST = 'challenge01.root-me.org'  # Hôte
PORT = 52002  # Port


def calcul(d):
    data = d.split('\n')
    line = data[6]
    nombres = re.findall(r'\d+', line)
    result = round(math.sqrt(int(nombres[0])) * int(nombres[1]), 2)
    return result
    

def main():
    try:
        # Connexion au serveur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        # Réception du message du serveur
        data = s.recv(1024).decode()
        print(data)

        res = str(calcul(data)) + '\n'

        # Envoi de la réponse au serveur
        s.send(str(res).encode(), 0)

        time.sleep(1)
        answer = s.recv(1024).decode()
        print(answer)
        
        s.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
