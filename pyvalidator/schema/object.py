from .exceptions import ValidationError
from .helpers import _extract_body_from_event

class Schema:
    def __init__(self, shape: dict):
        # shape: dict of field_name -> Field instance
        self.shape = shape or {}

    def validate(self, data_or_event):
        payload = _extract_body_from_event(data_or_event)
        if not isinstance(payload, dict):
            raise ValidationError({"_schema": "Payload inválido (esperado objeto JSON)"})

        out = {}
        errors = {}

        for name, field in self.shape.items():
            present = name in payload
            value = payload.get(name)
            try:
                if value is None and not present:
                    # Missing key
                    # We ask the field to validate None to check required
                    value = field.validate_value(None, name)
                else:
                    value = field.validate_value(value, name)
                if value is not None:
                    out[name] = value
            except ValidationError as ve:
                errors.update(ve.errors)

        if errors:
            raise ValidationError(errors)
        return out
