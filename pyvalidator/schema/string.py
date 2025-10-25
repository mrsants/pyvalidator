import re
from .base import Field
from ..validators.string_validators import is_email, is_alpha, is_empty, is_uuid, is_numeric, is_cpf, is_cnpj
from ..validators.web_validators import is_url

class StringField(Field):
    def __init__(self):
        super().__init__()
        self._validators.append((lambda v: isinstance(v, str), "Deve ser string"))

    def min(self, n, message=None):
        self._validators.append((lambda v, n=n: len(v) >= n, message or f"Min {n} caracteres"))
        return self

    def max(self, n, message=None):
        self._validators.append((lambda v, n=n: len(v) <= n, message or f"Max {n} caracteres"))
        return self

    def matches(self, pattern, flags=0, message="Formato inválido"):
        regex = re.compile(pattern, flags)
        self._validators.append((lambda v, r=regex: r.search(v) is not None, message))
        return self

    def email(self, message="E-mail inválido"):
        self._validators.append((lambda v: is_email(v), message))
        return self

    def url(self, message="URL inválida"):
        self._validators.append((lambda v: is_url(v), message))
        return self

    def uuid(self, message="UUID inválido"):
        self._validators.append((lambda v: is_uuid(v), message))
        return self

    def alpha(self, message="Apenas letras"):
        self._validators.append((lambda v: is_alpha(v), message))
        return self

    def numeric(self, message="Apenas números"):
        self._validators.append((lambda v: is_numeric(v), message))
        return self

    def cpf(self, message="CPF inválido"):
        self._validators.append((lambda v: is_cpf(v), message))
        return self

    def cnpj(self, message="CNPJ inválido"):
        self._validators.append((lambda v: is_cnpj(v), message))
        return self

def string():
    return StringField()
