class ValidationError(Exception):
    def __init__(self, errors):
        # errors: dict[str, str] mapping field -> error message
        self.errors = errors if isinstance(errors, dict) else {"_error": str(errors)}
        msg = "; ".join(f"{k}: {v}" for k, v in self.errors.items())
        super().__init__(msg)
