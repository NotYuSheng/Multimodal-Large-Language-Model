from mitmproxy import http, ctx

class MITMProxy:
    def __init__(self):
        self.target_host = "localhost"
        self.target_port = 11434

    def request(self, flow: http.HTTPFlow) -> None:
        # Modify the request host and port to forward to the target server
        flow.request.host = self.target_host
        flow.request.port = self.target_port
        ctx.log.info(f"Forwarding request to {self.target_host}:{self.target_port}")
        
    def response(self, flow: http.HTTPFlow) -> None:
        # Log the response
        ctx.log.info(f"Response: {flow.response.status_code}")

addons = [
    MITMProxy()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    import sys

    sys.argv = ["mitmdump", "-p", "5000", "-s", __file__]
    mitmdump()
