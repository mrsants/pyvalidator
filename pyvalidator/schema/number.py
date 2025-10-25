from .base import Field
from ..validators.number_validators import is_int, is_float, is_decimal

class NumberField(Field):
    def __init__(self):
        super().__init__()
        # allow int/float coercion in _coerce

    def _coerce(self, value):
        # Try to coerce strings to float
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            try:
                return float(value.replace(",", "."))
            except Exception:
                pass
        return value

    def min(self, n, message=None):
        self._validators.append((lambda v, n=n: isinstance(v, (int, float)) and v >= n, message or f"Min {n}"))
        return self

    def max(self, n, message=None):
        self._validators.append((lambda v, n=n: isinstance(v, (int, float)) and v <= n, message or f"Max {n}"))
        return self

    def integer(self, message="Deve ser inteiro"):
        self._validators.append((lambda v: isinstance(v, int) or (isinstance(v, float) and v.is_integer()), message))
        return self

def number():
    return NumberField()
