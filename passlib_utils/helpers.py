from passlib.context import CryptContext
from passlib_utils.schemas import argon2
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from passlib.ifc import PasswordHash
    from typing import Sequence


SCHEMAS = (argon2,)
DEPRECATED = ('auto',)


class PasswordHelper(CryptContext):
    def __init__(
        self,
        schemas: 'Sequence[PasswordHash]' = SCHEMAS,
        _autoload: bool = True,
        default: 'PasswordHash' = argon2,
        deprecated: 'Sequence[str]' = DEPRECATED,
        **kwargs
    ):
        super().__init__(schemas, _autoload=_autoload, default=default,
                         deprecated=deprecated, **kwargs)
