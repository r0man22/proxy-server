import socket
import ssl
import threading

HOST = "0.0.0.0"
PORT = 8888
CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

def handle_client(client_socket):
    try:
        request = client_socket.recv(4096)
        print(f"[REQUEST]\n{request.decode(errors='ignore')}")

        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect(("httpbin.org", 443))  
        secure_socket = ssl.wrap_socket(remote_socket)

        secure_socket.send(request)
        response = secure_socket.recv(4096)

        client_socket.send(response)

        secure_socket.close()
        client_socket.close()
    except Exception as e:
        print(f"[ERROR]: {e}")
        client_socket.close()

def start_proxy():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[PROXY] Proxy running on {HOST}:{PORT}...")

    while True:
        client_socket, addr = server.accept()
        print(f"[CONNECT] Connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_proxy()
