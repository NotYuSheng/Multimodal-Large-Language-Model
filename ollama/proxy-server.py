"""MITM Proxy Server Module."""

import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os
from mitmproxy import http

# Create 'logs' directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Generate log filename with current date
date_str = datetime.now().strftime("%Y%m%d")
log_filename = f"logs/ollama_traffic_{date_str}.log"

# Configure logging with rotation
handler = RotatingFileHandler(
    log_filename, maxBytes=50 * 1024 * 1024, backupCount=5
)  # 50 MB per file, 5 backups
logging.basicConfig(
    handlers=[handler], level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class MITMProxy:
    """MITM Proxy for logging HTTP requests and responses."""

    def __init__(self):
        """Initialize the proxy with target host and port."""
        self.target_host = "localhost"
        self.target_port = 11434

    def request(self, flow: http.HTTPFlow) -> None:
        """Handle incoming HTTP requests."""
        request_payload = flow.request.content
        max_log_size = 50 * 1024 * 1024  # 50 MB
        if len(request_payload) > max_log_size:
            logging.info(
                "Request: %s %s (payload truncated) %s...",
                flow.request.method,
                flow.request.url,
                request_payload[:max_log_size],
            )
        else:
            logging.info(
                "Request: %s %s %s",
                flow.request.method,
                flow.request.url,
                request_payload.decode("utf-8", "ignore"),
            )

        flow.request.host = self.target_host
        flow.request.port = self.target_port

    def response(self, flow: http.HTTPFlow) -> None:
        """Handle incoming HTTP responses."""
        response_payload = flow.response.content
        max_log_size = 50 * 1024 * 1024  # 50 MB
        if len(response_payload) > max_log_size:
            logging.info(
                "Response: %d (truncated) %s...",
                flow.response.status_code,
                response_payload[:max_log_size],
            )
        else:
            logging.info(
                "Response: %d %s",
                flow.response.status_code,
                response_payload.decode("utf-8", "ignore"),
            )

addons = [MITMProxy()]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    import sys

    sys.argv = ["mitmdump", "-p", "5000", "-s", __file__]
    mitmdump()
