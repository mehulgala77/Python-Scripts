
import socket
import os
import signal
import threading

# Utility class to handle graceful killing of the application.
class GracefulKiller():
    killNow = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, signum, frame):
        killNow = True


# The locking object
lock = threading.Lock()

# The list of connected clients
client = set()

# Graceful killer object
killer = GracefulKiller()

def communicate(clientSocket):

    # Add the client name in the global set
    lock.acquire()
    client.add(threading.current_thread().name)
    lock.release()

    while True:

        data = clientSocket.recv(1024)
        print(f"From {threading.current_thread().name} Data: {data}")

        if not data:
            print(f"No more data. Thread {threading.get_ident()} is dying. See you.")

            lock.acquire()
            client.remove(threading.current_thread().name)
            lock.release()

            break

        data = data[::-1]

        clientSocket.send(data)

    clientSocket.close()

def main():

    host = ""
    port = 12777

    print(f"Current process id: {os.getpid()}")
    print(f"Current thread is: {threading.main_thread().name}")

    # Create a TCP, Ipv4 server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket created.")

    # Bind the server socket to localhost and some custom port
    serverSocket.bind((host, port))
    print("Server socket bind to the host and the port.")

    # Enter the socket in the listening mode
    serverSocket.listen(5)
    print("Server socket put on the listening mode.")

    while killer.killNow == False:

        clientSocket, clientAddr = serverSocket.accept()

        print(f"Client {clientAddr[0]} : {clientAddr[1]} connected")

        thread = threading.Thread(target=communicate, args=(clientSocket,), name=str(clientAddr[1]))
        thread.setDaemon(True)
        thread.start()

    serverSocket.close()


if __name__ == "__main__":
    main()