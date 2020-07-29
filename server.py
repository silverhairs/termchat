import socket
import sys


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9090

try:
    server_socket.bind(("", port))
    server_socket.listen(5)
    print("Listening on port {}".format(port))
except socket.error as e:
    print("Failed with error: {}".format(e))
    sys.exit(1)

while True:

    connexion, address = server_socket.accept()
    print("{} joined the network🧐️🧐️\n".format(address))
    connexion.send(('Welcome').encode())
    msg = connexion.recv(1024).decode()
    print(msg)