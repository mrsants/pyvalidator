from .schema.object import Schema
from .schema.string import string
from .schema.number import number
from .schema.boolean import boolean
from .schema.exceptions import ValidationError

# Re-export common "is_*" validators for convenience
from .validators.string_validators import is_email, is_alpha, is_empty, is_uuid, is_numeric, is_cpf, is_cnpj
from .validators.web_validators import is_url, is_ip
from .validators.number_validators import is_int, is_float, is_decimal

__all__ = [
    "Schema",
    "string",
    "number",
    "boolean",
    "ValidationError",
    # is_* helpers
    "is_email", "is_alpha", "is_empty", "is_uuid", "is_numeric", "is_cpf", "is_cnpj",
    "is_url", "is_ip",
    "is_int", "is_float", "is_decimal",
]
