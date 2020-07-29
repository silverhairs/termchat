import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(("127.0.0.1", 9090))

    while True:
        if client_socket.recv:
            print(client_socket.recv(1024).decode())
            msg = input('➡️ ')
            client_socket.sendall(msg.encode())

except socket.error as e:
    print("Failed with error: {}".format(e))

