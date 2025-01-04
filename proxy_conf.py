import http.server
import socketserver
import http.client
import ssl

class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = self.path
        
        try:
            connection = http.client.HTTPConnection("example.com", 80)
            connettion.request("GET", target_url)
            response = connection.getresponse()
            
            self.send_response(response.status)
            self.send_header('Content-Type', response.getheader('Content-Type'))
            self.end_headers()
            self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Proxy Error: {e}")

    def do_POST(self):
        target_url = self.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
    
        try:
            connection = http.client.HTTPConnection("example.com", 80)
            conntection.request("POST", target_url, body=post_data, headers=dict(self.headers))
            response = connection.getresponse()
          
            self.send_response(response.status)
            self.send_header('Content-Type', response.getheader('Content-Type'))
            self.end_headers()
            self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Proxy Error: {e}")

port = 8080

with socketserver.TCPServer(("", port), ProxyHTTPRequestHandler) as httpd:

    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="mitm.key", certfile="mitm.crt", server_side=True)

httpd.serve_forever()
