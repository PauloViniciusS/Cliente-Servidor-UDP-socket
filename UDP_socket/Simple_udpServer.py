'''
Código para criação de um servidor UDP para estudo de socket, tem a função de se comunicar com o cliente
UDP e por meio da conexão, receber comandos remotos.
'''

import subprocess
from socket import *

serverPort = 12500 # Necessário definir a porta para conexão com o cliente UDP, padrão para ambos
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    command = message.decode('utf-8')
    print("Received from Client: ", command)

    try:
        output = subprocess.check_output(command, shell=True)

        # Conversão para bytes
        output_bytes = output.strip()

        # Enviar a conversão para o cliente
        serverSocket.sendto(output_bytes, clientAddress)

    except Exception as e:
        # Mensagem de erro para o cliente
        error_message = str(e)
        print("Error: ", error_message)

        error_bytes = error_message.encode('utf-8')
        serverSocket.sendto(error_bytes, clientAddress)
