from base64 import urlsafe_b64decode, urlsafe_b64encode
from datetime import datetime, timedelta
from hashlib import sha3_512
import hmac
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class BaseHelper:
    pass


class TokenHelper(BaseHelper):
    cypher: 'Any'

    def __init__(self, secret: bytes):
        self.secret = secret

    def generate_token(self, identity):
        expired_at = datetime.now() + timedelta(hours=24)
        expired_at = str(int(expired_at.timestamp()))
        token_data = f'{expired_at}${identity}'
        token_data = token_data.encode('utf-8')
        token_hash = hmac.digest(self.secret, token_data, 'sha3-512')
        token = f'{token_data}${token_hash}'
        token = token.encode('utf-8')
        token = urlsafe_b64encode(token)
        return token

    def verify_token(self, token: str):
        token = token.encode('utf-8')
        token = urlsafe_b64decode(token)
        token = token.decode('utf-8')
        identity, expired = token.split('$')
        return identity, expired
