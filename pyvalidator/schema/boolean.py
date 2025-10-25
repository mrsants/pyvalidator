from .base import Field

class BooleanField(Field):
    def __init__(self):
        super().__init__()

    def _coerce(self, value):
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            v = value.strip().lower()
            if v in ("true", "1", "yes", "y", "sim"):
                return True
            if v in ("false", "0", "no", "n", "nao", "não"):
                return False
        return value

def boolean():
    return BooleanField()
