from urllib.parse import urlparse
import ipaddress

def is_url(value: str, require_protocol=True) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlparse(value)
        if require_protocol and not parsed.scheme:
            return False
        return bool(parsed.netloc)
    except Exception:
        return False

def is_ip(value: str) -> bool:
    if not isinstance(value, str):
        return False
    try:
        ipaddress.ip_address(value)
        return True
    except Exception:
        return False
