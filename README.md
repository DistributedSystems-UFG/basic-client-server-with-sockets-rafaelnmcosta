[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)

## calculadora implementada;
O server fica aguardando conexões, quando um client se conecta, o server entra em um loop recebendo mensagens.

O client envia uma expressão matemática no formato "numero operador numero" (COM O ESPAÇO):
Ex:
10 + 5
7 * 3
20 / 4  
As operações suportadas são:
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
(os valores são convertidos pra float)

O server recebe a mensagem, calcula a operação e retorna o resultado para o client.

O client imprime o resultado recebido do server no final.
