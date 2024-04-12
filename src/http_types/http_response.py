from typing import Dict

class HTTPResponse:
    def __init__(self, body: Dict, status_code: int):
        self.body = body
        self.status_code = status_code