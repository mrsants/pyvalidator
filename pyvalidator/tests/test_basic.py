import json
from pyvalidator import Schema, string, number, boolean, ValidationError

def test_happy_path():
    schema = Schema({
        "email": string().required().email(),
        "cpf": string().required().cpf(),
        "age": number().min(18).max(99),
        "ok": boolean().optional(),
    })
    event = {"body": json.dumps({"email":"a@b.com","cpf":"390.533.447-05","age": 30,"ok":"true"})}
    got = schema.validate(event)
    assert got["email"] == "a@b.com"
    assert got["cpf"]
    assert got["age"] == 30
    assert got["ok"] is True

def test_error():
    schema = Schema({"email": string().required().email()})
    try:
        schema.validate({"body": json.dumps({"email":"not"})})
    except ValidationError as e:
        assert "email" in e.errors
