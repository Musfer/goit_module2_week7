import socket

HEADER = 64
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!DISCONNECT"
TCP_PORT = 5050
TCP_IP = 'localhost'
SERVER = (TCP_IP, TCP_PORT)


def send(msg: str, server: (str, int) = SERVER):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server)
        print(f"Connection established {server}")
        sentences = msg.split("\n")
        for sentence in sentences:
            print(f"Sending data: {sentence}")
            sock.send(sentence.encode(FORMAT))
            response = sock.recv(HEADER).decode(FORMAT)
            print(f"Server response: {response}")
    print(f"Data transfer completed")


if __name__ == "__main__":
    send("Hello!\nHow are you?")
    send("Got my message?")
