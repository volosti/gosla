from datetime import datetime, timedelta
import secrets
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any



print(secrets.token_urlsafe())
print(secrets.token_bytes())
print(secrets.token_hex())
print()



class PasswordEmailRecoverMixin:
    actor: 'Any'  # entity must have `identity` attribute
    password_recover_helper: 'Any'

    def send_recover_token_by_email(self):
        identity = self.actor.identity
        return self.password_recover_helper.generate_token(identity)

    def generate_recover_token(self):
        identity = self.actor.identity
        return self.password_recover_helper.generate_token(identity)

    def verify_recover_token(self, token):
        return self.password_recover_helper.verify_token()


class PasswordPhoneRecoverMixin:
    recover_code_min_value: int = 10013
    recover_code_max_value: int = 99987
    recover_code_retry: int = 3
    recover_code_expiry: timedelta = timedelta(minutes=5)

    def generate_recover_code(self):
        return str(secrets.choice(range(10013, 99987)))

    def verify_recover_code(self, code):
        pass
