#Port Number: 20
import os
import pickle
import socket
import _thread

def thread(server, connect, data):
    parsed = data.split(" ")                #Parse input
    if(parsed[0] == "LIST"):                #If LIST then list files
        path = os.getcwd()
        files = os.listdir(path);
        filesList = pickle.dumps(files)
        connect.send(filesList)
    elif(parsed[0] == "RETRIEVE"):          #If RETRIEVE then return file
        file = open(parsed[1], "r")
        chunk = file.read(1024)
        while(chunk):
            connect.send(chunk)
            chunk = file.read(1024)
    elif(parsed[0] == "STORE"):             #If STORE then save file
        filename = open(parsed[1], "w")
        while(True):
            file = server.recv(1024).decode()
            if not file:
                break
            filename.write(file)
    elif(parsed[0] == "QUIT"):              #IF QUIT then close the connection
        server.close()
    else:
        print("Invalid Command")            #Catch invalid inputs

host = socket.gethostname()                 #Hostname of server
port = 20                                   #Port number for FTP

serverSocket = socket.socket()              #instance of socket
serverSocket.bind((host, port))             #bind host and port

serverSocket.listen(3)
while True:                                 #Continue listening
    connect, address = serverSocket.accept()
    data = connect.recv(1024).decode()
    _thread.start_new_thread(thread, (serverSocket, connect, str(data)))