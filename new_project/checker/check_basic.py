import jsonschema
from jsonschema import validate

def check_status_code(resp, expected_status):
    msg = f'Ожидаемый статус: {expected_status}; Фактический статус: {resp.status_code}'
    assert resp.status_code == expected_status, msg

def check_valid_schema(instance, schema):
    """Проверка валидности JSON-схемы"""
    try:
        validate(instance, schema)
    except jsonschema.ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e}")

def check_json_has_keys(data, expected_keys):
    """Проверка, что JSON-объект содержит все ключи из списка"""
    assert isinstance(data, dict), "Response не является объектом JSON"
    msg = set(expected_keys) - set(data.keys())
    assert not msg, f"Отсутствующие ключи: {msg}"

def check_json_value(data, key, expected_value):
    """Проверка, что значение по ключу совпадает с ожидаемым"""
    msg = f"Ключ: '{key}', ожидаемое значение - {expected_value}, фактическое - {data.get(key)}"
    assert data.get(key) == expected_value, msg
        