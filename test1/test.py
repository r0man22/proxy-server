import ssl
import socket

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
context.load_verify_locations(cafile="ca-cert.pem")  # CA sertifikası

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))  # Sunucu IP ve port
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    
    secure_socket = context.wrap_socket(client_socket, server_side=True)
    
    print("Bağlantı kuruldu:", addr)
    secure_socket.send(b"Hello, secure world!")  # Güvenli bağlantıyı doğrulamak için mesaj gönder
    secure_socket.close()
