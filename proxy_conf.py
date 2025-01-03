import http.server
import socketserver

class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		target_url =
