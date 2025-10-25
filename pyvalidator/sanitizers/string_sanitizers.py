import html
import re
import unicodedata

def trim(value: str, chars=None) -> str:
    if not isinstance(value, str):
        return value
    return value.strip(chars) if chars else value.strip()

def escape(value: str) -> str:
    if not isinstance(value, str):
        return value
    return html.escape(value)

def unescape(value: str) -> str:
    if not isinstance(value, str):
        return value
    return html.unescape(value)

def strip_low(value: str, keep_new_lines=False) -> str:
    if not isinstance(value, str):
        return value
    pattern = r"[\x00-\x1F\x7F]" if keep_new_lines else r"[\x00-\x1F\x7F\r\n]"
    return re.sub(pattern, '', value)

def normalize(value: str) -> str:
    if not isinstance(value, str):
        return value
    return unicodedata.normalize("NFKC", value)

def remove_accents(value: str) -> str:
    if not isinstance(value, str):
        return value
    nkfd = unicodedata.normalize('NFKD', value)
    return ''.join([c for c in nkfd if not unicodedata.combining(c)])
