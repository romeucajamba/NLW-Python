from typing import Dict

class HTTPResquest:
    def __init__(self, param: Dict = None, body: Dict = None) -> None:
        self.param = param
        self.body = body