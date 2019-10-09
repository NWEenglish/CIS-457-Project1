#Port Number: 20

import socket as socket

host = socket.gethostname()     #Hostname of server
port = 20                       #Port number for FTP

serverSocket = socket.socket()  #instance of socket
serverSocket.bind((host, port)) #bind host and port