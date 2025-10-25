from .exceptions import ValidationError

class Field:
    def __init__(self):
        self._required = False
        self._optional = False
        self._validators = []   # list of (callable(value) -> bool, error_message)
        self._transforms = []   # list of callables to transform value before validate

    def required(self, message="Campo obrigatório"):
        self._required = True
        return self

    def optional(self):
        self._optional = True
        self._required = False
        return self

    def transform(self, func):
        self._transforms.append(func)
        return self

    def _run_validators(self, value, field_name):
        for fn, msg in self._validators:
            try:
                ok = fn(value)
            except Exception:
                ok = False
            if not ok:
                raise ValidationError({field_name: msg})

    def _apply_transforms(self, value):
        for t in self._transforms:
            value = t(value)
        return value

    def _coerce(self, value):
        # Override in subclasses
        return value

    def validate_value(self, value, field_name):
        if value is None:
            if self._required:
                raise ValidationError({field_name: "Campo obrigatório"})
            return None
        value = self._apply_transforms(value)
        value = self._coerce(value)
        self._run_validators(value, field_name)
        return value
