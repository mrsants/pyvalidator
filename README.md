# pyvalidator

`pyvalidator` is a lightweight validation library for Python, inspired by **Yup (JavaScript)** and **validator.js**, designed to be clean, chainable, and compatible with serverless environments such as AWS Lambda.

It supports schema-based validation, standalone `is_*` functions (like `is_email`, `is_cpf`, etc.), and can validate raw AWS Lambda events transparently.

---

## Installation

```bash
pip install -e .
```

or if published later:

```bash
pip install pyvalidator
```

---

## Key Features

* Schema-based validation similar to Yup (`string().required().email()`).
* Built-in validations: email, URL, UUID, CPF, CNPJ, numeric, alpha.
* Accepts raw AWS Lambda `event` objects directly (API Gateway, SQS, SNS).
* Functional validators (`is_email`, `is_url`, `is_cpf`, etc.) similar to validator.js.
* Basic sanitizers included (trim, escape, normalize_email).
* No external dependencies.

---

## Basic Usage

### Schema validation

```python
from pyvalidator import Schema, string, number, boolean, ValidationError

user_schema = Schema({
    "email": string().required().email(),
    "cpf": string().required().cpf(),
    "age": number().min(18).max(99),
    "website": string().url().optional(),
    "is_active": boolean().optional(),
})

def handler(event, context):
    try:
        data = user_schema.validate(event)  # accepts full AWS Lambda event
        return {"statusCode": 200, "body": "validated"}
    except ValidationError as e:
        return {"statusCode": 400, "body": str(e.errors)}
```

### Direct use of validators

```python
from pyvalidator import is_email, is_url, is_cpf

is_email("test@mail.com")   # True
is_url("https://example.com")  # True
is_cpf("390.533.447-05")    # True
```

---

## Available Field Types

| Method       | Description                 |
| ------------ | --------------------------- |
| `string()`   | String validation           |
| `number()`   | Integer/float validation    |
| `boolean()`  | Boolean coercion/validation |
| `Schema({})` | Object/schema validation    |

---

## String Field - Methods

| Method            | Description                        |
| ----------------- | ---------------------------------- |
| `.required()`     | Field must be present and non-null |
| `.optional()`     | Field is optional                  |
| `.email()`        | Valid email address                |
| `.url()`          | Valid URL                          |
| `.uuid()`         | Valid UUID                         |
| `.cpf()`          | Valid Brazilian CPF                |
| `.cnpj()`         | Valid Brazilian CNPJ               |
| `.min(n)`         | Minimum number of characters       |
| `.max(n)`         | Maximum number of characters       |
| `.matches(regex)` | Must match regex                   |

---

## Number Field - Methods

| Method       | Description           |
| ------------ | --------------------- |
| `.min(n)`    | Minimum numeric value |
| `.max(n)`    | Maximum numeric value |
| `.integer()` | Must be an integer    |

---

## Sanitization Examples

```python
from pyvalidator.sanitizers.string_sanitizers import trim, escape
from pyvalidator.sanitizers.email_sanitizers import normalize_email

trim("  test  ")             # "test"
escape("<script>")           # "&lt;script&gt;"
normalize_email("Foo.Bar@gmail.com")  # "foobar@gmail.com"
```

---

## Project Structure

```
pyvalidator/
├── __init__.py
├── schema/                 # Yup-style schema (string(), number(), boolean(), Schema)
├── validators/             # Functional-style validators (is_email, is_cpf, etc.)
├── sanitizers/             # trim, escape, normalize_email
├── tests/
└── setup.py
```

---

## Roadmap

* `.strip_unknown()` for removing unexpected fields
* `.nullable()`, `.one_of()`, `.not_one_of()`
* `.date()` and ISO8601 validation
* CEP and Brazilian phone validation
* PyPI publishing
* Automatic Lambda Layer packaging
