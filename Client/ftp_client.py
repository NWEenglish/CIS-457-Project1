# This is an FTP Client that communicates with an FTP Server. Code was written for CIS 457 at GVSU.
#
# Authors:  Denver DeBoer
#           Nicholas English
#           Kevin Smith
# Date:     10-14-2019

import socket
import json
import select


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Main
def main():
    try:
        startup()
    finally:
        quit()


# Starts the program execution.
def startup():
    print('\n\nWelcome to FTP Client!\n\n')
    print('Listed below are the commands. Enter \'HELP\' if you forget!')
    help()
    beginUI()


# User interface
def beginUI():
    command = input(' ~ ')
    command = command.split()

    # Check the input
    if not command:
        pass
    elif command[0].upper() == 'HELP' and len(command) == 1:
        help()
    elif command[0].upper() == 'CONNECT' and len(command) == 3:
        connect(command[1], command[2])
    elif command[0].upper() == 'LIST' and len(command) == 1:
        listFiles()
    elif command[0].upper() == 'RETRIEVE' and len(command) == 2:
        retrieve(command[1])
    elif command[0].upper() == 'STORE' and len(command) == 2:
        store(command[1])
    elif command[0].upper() == 'QUIT' and len(command) == 1:
        quitConnection()
    elif command[0].upper() == 'CLOSE' and len(command) == 1:
        return
    else:
        print('\n ERROR - Something went wrong!\n\t Command ' + command[0].upper() + ' caused an error!\n')

    beginUI()


# Prints to the user the available commands.
def help():
    print('\n\n-------------------- Commands --------------------')
    print('CONNECT <SERVER NAME/IP ADDRESS> <SERVER PORT>')
    print('LIST')
    print('RETRIEVE <FILENAME>')
    print('STORE <FILENAME>')
    print('QUIT')
    print('HELP')
    print('CLOSE')
    print('--------------------------------------------------\n\n')


def connect(serverName, serverPort):
    try:
        print(' Connecting...')

        serverAddress = (str(serverName), int(serverPort))
        sock.connect(serverAddress)

        print(' Connected!')

    except:
        print(' ERROR - Could NOT connect to server!')


# Requests the server to list available files.
def listFiles():
    print(' Getting files stored on the server...')
    try:
        msg = 'LIST'
        print('\n--------------------------------------------------')
        sendMessage(msg)

        while True:
            try:
                files = sock.recv(1024)
            except:
                pass
            else:
                files = json.loads(files.decode())
                fileList = files.get("FILES")
                print(*fileList, sep=', ')
                break
        print('--------------------------------------------------')
    except:
        print(' ERROR - Could NOT get list!')


# Requests the server to send the specified file.
def retrieve(filename):
    print(" RETRIEVING DATA...")
    msg = "RETRIEVE " + filename
    sock.sendall(msg.encode())
    file = open(filename, 'w')
    totalData = []
    data = ''

    while (True):
        ready = select.select([sock], [], [], 2)
        if (ready[0]):
            data = sock.recv(1024).decode()
        else:
            break
        totalData.append(data)
        file.write(''.join(totalData))
        file.close()
        print(" DATA RETRIEVED!\n")


# Requests the server to keep the specified file.
def store(filename):
    try:
        print(" STORING DATA...")
        msg = 'STORE ' + filename
        sock.sendall(msg.encode())
        file = open(filename, "rb")
        sock.sendall(file.read(1024))
        print(' DATA STORED!')
    except:
        print(' ERROR - File could NOT be stored!')

    try:
        file.close()
    except:
        print(' ERROR - File could NOT be closed! This may be caused due to the file not existing.')


# Terminates connection with server.
def quitConnection():
    print(' Terminating connection...')
    try:
        msg = 'QUIT'
        sendMessage(msg)
        sock.close()
    except:
        print(' An error has occurred! This may be caused due to no connection.')

    print(' Connection terminated!')


# Sends the message to the server.
def sendMessage(msg):
    try:
        # print("Sending %s" % msg)
        sock.sendall(msg.encode())
    except:
        print(' ERROR - Request NOT sent to server!')


main()
