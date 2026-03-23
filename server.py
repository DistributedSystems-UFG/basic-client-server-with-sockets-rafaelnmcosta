from socket  import *
from constCS import * #-

def calcular(expressao):
    try:
        partes = expressao.strip().split()

        if len(partes) != 3:
            return "formato inválido"

        a, op, b = partes
        a = float(a)
        b = float(b)

        if op == '+':
            return str(a + b)
        elif op == '-':
            return str(a - b)
        elif op == '*':
            return str(a * b)
        elif op == '/':
            if b == 0:
                return "divisão por zero"
            return str(a / b)
        else:
            return "operador inválido"

    except Exception:
        return "Erro"


s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
	data = conn.recv(1024)   # receive data from client
	if not data: break       # stop if client stopped
	mensagem = data.decode()
    	print(f"Recebido: {mensagem}")

    	resultado = calcular(mensagem)

    	conn.send(resultado.encode())
conn.close()               # close the connection
