from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

while True:
    msg = input("Digite a operação (ex: 10 + 5) ou 'sair': ")

    if msg.lower() == 'sair':
        break

    s.send(msg.encode())

    data = s.recv(1024)
    print("Resultado:", data.decode())
s.close()               # close the connection
