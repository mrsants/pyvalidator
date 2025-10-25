def normalize_email(email: str, all_lowercase=True, gmail_remove_dots=True):
    if not isinstance(email, str):
        return email
    email = email.strip()
    if all_lowercase:
        email = email.lower()
    local, sep, domain = email.partition("@")
    if not sep:
        return email
    if domain in ("gmail.com", "googlemail.com") and gmail_remove_dots:
        local = local.replace(".", "")
    return f"{local}@{domain}"
