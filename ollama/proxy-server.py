from mitmproxy import http, ctx
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with rotation
handler = RotatingFileHandler('ollama_traffic.log', maxBytes=50*1024*1024, backupCount=5)  # 50 MB per file, 5 backups
logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MITMProxy:
    def __init__(self):
        self.target_host = "localhost"
        self.target_port = 11434

    def request(self, flow: http.HTTPFlow) -> None:
        # Log request details including payload
        request_payload = flow.request.content
        max_log_size = 50 * 1024 * 1024  # 50 MB
        if len(request_payload) > max_log_size:
            # Log a truncated version of the request payload
            logging.info(f"Request: {flow.request.method} {flow.request.url} (payload truncated) {request_payload[:max_log_size]}...")
        else:
            # Log the full request payload
            logging.info(f"Request: {flow.request.method} {flow.request.url} {request_payload.decode('utf-8', 'ignore')}")

        # Forward request to the target server
        flow.request.host = self.target_host
        flow.request.port = self.target_port

    def response(self, flow: http.HTTPFlow) -> None:
        # Log response details including payload
        response_payload = flow.response.content
        max_log_size = 50 * 1024 * 1024  # 50 MB
        if len(response_payload) > max_log_size:
            # Log a truncated version of the response payload
            logging.info(f"Response: {flow.response.status_code} (truncated) {response_payload[:max_log_size]}...")
        else:
            # Log the full response payload
            logging.info(f"Response: {flow.response.status_code} {response_payload.decode('utf-8', 'ignore')}")

addons = [
    MITMProxy()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    import sys

    sys.argv = ["mitmdump", "-p", "5000", "-s", __file__]
    mitmdump()
