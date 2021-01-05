from datetime import datetime, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class EmailRecoverHelper:
    cypher: Any

    def __init__(self, secret):
        self.secret = secret

    def gen_token(self, info):
        expired = str(int((datetime.now() + timedelta(hours=24)).timestamp()))
        secret: str = self.secret
        f'{expired}${info}${secret}'.encode('utf-8')

    def verify_token(self, token):
        token = self.decode(token)

    def encode(self, data: str):
        pass

    def decode(self, token: bytes):
        pass
