import mitmproxy
import logging

class HttpRequestLogger:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        # HTTP isteği geldiğinde bu fonksiyon çalışacak
        logging.info(f"HTTP isteği alındı: {flow.request.method} {flow.request.url}")
        # İsteği değiştirebilirsiniz
        # flow.request.headers["User-Agent"] = "Custom User-Agent"

addons = [HttpRequestLogger()]
