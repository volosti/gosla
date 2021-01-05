from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Dict, Iterable, Tuple
    from gosla.validation.validators import BaseValidator


class ValidatorMixin:
    password_validators: 'Iterable[BaseValidator]'

    def validate_password(self, secret: str):
        result: 'Dict[str, Any]' = {}
        for validator in self.password_validators:
            key, value = validator.validate(secret)
            result[key] = value
        return result
