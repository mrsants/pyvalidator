def is_int(value) -> bool:
    if isinstance(value, int):
        return True
    if isinstance(value, str):
        try:
            int(value)
            return True
        except Exception:
            return False
    return False

def is_float(value) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, str):
        try:
            float(value.replace(",", "."))
            return True
        except Exception:
            return False
    return False

def is_decimal(value) -> bool:
    return is_float(value)
