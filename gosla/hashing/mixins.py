from gosla import PasswordHelper
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from passlib.context import CryptContext
    from typing import Optional, Tuple


class PasswordMixin:
    """
    Password mixin for user data model
    """
    password: 'Optional[str]'
    password_helper: 'CryptContext' = PasswordHelper()

    def dummy_verify_password(self):
        self.password_helper.dummy_verify()

    def set_password(self, password: str) -> None:
        self.password = self.password_helper.hash(password)

    def verify_password(self, password: str) -> 'Tuple[bool, bool]':
        verified, replacement_hash = self.password_helper.verify_and_update(
            secret=password,
            hash=self.password,
        )
        if need_save := bool(replacement_hash):
            self.set_password(replacement_hash)
        return verified, need_save
