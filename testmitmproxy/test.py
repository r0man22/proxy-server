import mitmproxy
import logging

class HttpRequestLogger:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        logging.info(f"HTTP isteği alındı: {flow.request.method} {flow.request.url}")

addons = [HttpRequestLogger()]
