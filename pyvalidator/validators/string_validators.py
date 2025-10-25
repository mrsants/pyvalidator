import re
import uuid

def is_empty(value: str, ignore_whitespace=True) -> bool:
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    return value.strip() == "" if ignore_whitespace else value == ""

def is_alpha(value: str) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", value))

def is_numeric(value: str) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r"\d+", value))

def is_email(value: str) -> bool:
    if not isinstance(value, str):
        return False
    # permissive but practical regex
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value) is not None

def is_uuid(value: str) -> bool:
    if not isinstance(value, str):
        return False
    try:
        uuid.UUID(value)
        return True
    except Exception:
        return False

def _only_digits(s):
    return re.sub(r"\D", "", s or "")

def is_cpf(value: str) -> bool:
    # Brazilian CPF validation
    s = _only_digits(value)
    if len(s) != 11 or s == s[0] * 11:
        return False
    # first check digit
    sum1 = sum(int(s[i]) * (10 - i) for i in range(9))
    d1 = (sum1 * 10) % 11
    d1 = 0 if d1 == 10 else d1
    # second check digit
    sum2 = sum(int(s[i]) * (11 - i) for i in range(10))
    d2 = (sum2 * 10) % 11
    d2 = 0 if d2 == 10 else d2
    return s[-2:] == f"{d1}{d2}"

def is_cnpj(value: str) -> bool:
    # Brazilian CNPJ validation
    s = _only_digits(value)
    if len(s) != 14 or s == s[0] * 14:
        return False
    def calc_digit(numbers, weights):
        total = sum(int(n) * w for n, w in zip(numbers, weights))
        r = total % 11
        return "0" if r < 2 else str(11 - r)
    w1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    w2 = [6] + w1
    d1 = calc_digit(s[:12], w1)
    d2 = calc_digit(s[:12] + d1, w2)
    return s[-2:] == d1 + d2
