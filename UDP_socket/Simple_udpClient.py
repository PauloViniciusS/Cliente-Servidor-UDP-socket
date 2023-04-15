'''
Código para criação de um cliente UDP para estudo de socket, tem a função de se comunicar com o servidor
UDP e por meio da conexão, enviar comandos remotos.
'''
import subprocess 
from socket import *
import chardet
import time

serverName = "127.0.0.1" # Necessário definir o endereço ip do servidor UDP, padrão para ambos
serverPort = 12500       # Necessário definir a porta para conexão com o servidor UDP, padrão para ambos
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("UDP Client\n")

# Comando é inserido aqui para o servidor
command = "shutdown -s -t 1000" 

# Codificação da cadeia de caracters como bytes
command_bytes = command.encode()

# Envio do comando para o servidor
clientSocket.sendto(command_bytes, (serverName, serverPort))

# Criação do buffer, necessário definir de acordo com o que deve enviado
output_bytes, serverAddress = clientSocket.recvfrom(4096)

# Detecta a codificação da resposta usando chardet
output_encoding = chardet.detect(output_bytes)['encoding']

# Decodificação da cadeia de bytes como caracteres usando o codec correto
output = output_bytes.decode(output_encoding)

print(output)

