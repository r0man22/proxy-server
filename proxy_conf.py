import http.server
import socketserver

class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = self.path 

        connection = http.client.HTTPConnection(target_url)
        connection.request("GET", target_url)
        response = connection.getresponse()

        self.send_response(response.status)
        self.send_header('Content-Type', response.getheader('Content-Type'))
        self.end_headers()
        self.wfile.write(response.read())

    def do_POST(self):
        target_url = self.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        connection = http.client.HTTPConnection(target_url)
        connection.request("POST", target_url, body=post_data, headers=self.headers)
        response = connection.getresponse()

        self.send_response(response.status)
        self.send_header('Content-Type', response.getheader('Content-Type'))
        self.end_headers()
        self.wfile.write(response.read())

port = 8080  
with socketserver.TCPServer(("", port), ProxyHTTPRequestHandler) as httpd:
    print(f"Proxy sunucusu {port} numaralı portta çalışıyor...")
    httpd.serve_forever()
