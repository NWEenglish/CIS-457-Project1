
from ftplib import FTP









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
    
    print('COMMAND: ')
    
    
    

# Prints to the user the available commands.
def help():
    print('\n\n-------------------- Commands --------------------')
    print('CONNECT <SERVER NAME/IP ADDRESS> <SERVER PORT>')
    print('LIST')
    print('RETRIEVE <FILENAME>')
    print('STORE <FILENAME>')
    print('QUIT')
    print('--------------------------------------------------\n\n')


# Connects to the server.
def connect(serverName, serverPort):
    FTP.connect(host = serverName, port = serverPort)
    

# Requests the server to list available files.
def list():
    print('QUIT')
    

# Requests the server to send the specified file.
def retrieve(fileName):
    print('QUIT')
    
# Requests the server to keep the specified file.
def store(fileName):
    print('QUIT')
    
# Terminates connection with server.
def quit():
    print('Terminating connection...')
    FTP.close()
    print('Connection has been terminated!')
    

# Begin file execution.
main()




