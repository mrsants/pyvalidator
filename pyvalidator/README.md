# pyvalidator

Validaçãoe helpers, leve e amigável para **AWS Lambda**.

## Uso

```python
from pyvalidator import Schema, string, number, ValidationError

user_schema = Schema({
    "email": string().required().email(),
    "cpf": string().required().cpf(),
    "age": number().min(18).max(99),
})

def handler(event, context):
    try:
        data = user_schema.validate(event)  # pode enviar o event bruto da Lambda
        return {"statusCode": 200, "body": "ok"}
    except ValidationError as e:
        return {"statusCode": 400, "body": str(e.errors)}
```

## Instalação local

```bash
pip install -e .
```
