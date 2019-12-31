
import socket
import os

def main():

    host = "127.0.0.1"
    port = 12777

    print(f"Current process id: {os.getpid()}")

    # Create a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client socket created")

    # Connect to the Server
    clientSocket.connect((host, port))
    print("Connected to the Server")

    message = "Hello from Jon!"

    while True:

        clientSocket.send(message.encode("ASCII"))

        serverMessage = clientSocket.recv(1024)

        print(f'Server message is {serverMessage.decode("ASCII")}')

        user = input("\nDo you want to continue(y/n)?")
        if user == "y":
            continue
        else:
            break

    clientSocket.close()


if __name__ == '__main__':
    main()