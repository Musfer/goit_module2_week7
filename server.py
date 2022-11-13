import socket
from concurrent import futures as cf


FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!DISCONNECT"
TCP_PORT = 5050
TCP_IP = 'localhost'
SERVER = (TCP_IP, TCP_PORT)


def handle_client(sock: socket.socket, addr: str):
    print(f"NEW CONNECTION: {addr} connected.")
    while True:
        received = sock.recv(1024)
        if not received:
            break
        data = received.decode()
        print(f"Data received: {data}")
        print(f"Sending response ...")
        sock.send("OK".encode(FORMAT))

    sock.close()


def run_server(server: (str, int) = SERVER):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server)
    server_socket.listen(12)  # listen up to 12 clients
    print(f"Server is listening on {server_socket.getsockname()}")
    with cf.ThreadPoolExecutor(12) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()
                client_pool.submit(handle_client, new_sock, address)
        except KeyboardInterrupt:
            print(f"Destroy sever")
        finally:
            server_socket.close()


if __name__ == "__main__":
    run_server()
