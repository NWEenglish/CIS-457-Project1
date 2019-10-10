
import sys
import socket
from ftplib import FTP
ftp = FTP()

# Main
def main():
    startup()
    

# Starts the program execution.
def startup():
    print('\n\nWelcome to FTP Client!\n\n')
    print('Listed below are the commands. Enter \'HELP\' if you forget!')
    help()
    beginUI()
    

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
        list()
    
    elif command[0].upper() == 'RETRIEVE' and len(command) == 2:
        retrieve(command[1])
    
    elif command[0].upper() == 'STORE' and len(command) == 2:
        store(command[1])
    
    elif command[0].upper() == 'QUIT' and len(command) == 1:
        quit()
    
    elif command[0].upper() == 'EXIT' and len(command) == 1:
        exit()
    
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
    print('EXIT')
    print('--------------------------------------------------\n\n')


# Connects to the server.
def connect(serverName, serverPort):
    if serverName.upper() == 'LOCALHOST':
        serverName = socket.gethostname()
        
    try:
        ftp.connect(host = serverName, port = int(serverPort))
    except:
        print(' An error has occured! This may be caused due to an invalid host or the server is closed.')
    
    if not ftp:
        print(' Connection was not established!')
    else:
        print(' Connected!')

# Requests the server to list available files.
def list():
    print(' Getting files stored on server...')
    print('\n--------------------------------------------------')
    try:
        ftp.sendcmd('LIST')
    except:
        print(' An error has occured! This may be caused due to no connection.')
    print('--------------------------------------------------')

# Requests the server to send the specified file.
def retrieve(fileName):
    print(' Getting file from server...')
    localfile = open(fileName, 'wb')
    try:
        ftp.retrlines('RETRIEVE ' + fileName, localfile.write, 1024)
    except:
        print(' An error has occured! This may be caused due to no connection or an incorrect file name.')
    
    
# Requests the server to keep the specified file.
def store(fileName):
    print(' Sending file to server...')
    try:
        ftp.storlines('STORE ' + fileName, open(fileName, 'r'))
        print(' File has been stored!')
    except:
        print(' An error has occured! This may be caused due to no connection.')
        print(' ERROR - File was not stored!')
    
# Terminates connection with server.
def quit():
    print(' Terminating connection...')
    try:
        ftp.sendcmd('QUIT')
        ftp.close()
    except:
        print(' An error has occured! This may be caused due to no connection.')
    print(' Connection terminated!')

# Quits the program.
def exit():
    print(' Exiting program...')
    print(' Thank you for using FTP Client!\n\n\n')
    sys.exit(0)
    

# Begin file execution.
main()




