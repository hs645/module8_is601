# tests/integration/test_fastapi_calculator.py

import json
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:8000"


def _post_operation(path: str, payload: dict):
    """
    Helper function to send POST requests to the running FastAPI server.
    Returns a tuple of (status_code, response_json).
    """
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode()
            return response.status, json.loads(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        return exc.code, json.loads(body)


def test_add_api(fastapi_server):
    status, data = _post_operation("/add", {"a": 10, "b": 5})
    assert status == 200
    assert data["result"] == 15


def test_subtract_api(fastapi_server):
    status, data = _post_operation("/subtract", {"a": 10, "b": 5})
    assert status == 200
    assert data["result"] == 5


def test_multiply_api(fastapi_server):
    status, data = _post_operation("/multiply", {"a": 10, "b": 5})
    assert status == 200
    assert data["result"] == 50


def test_divide_api(fastapi_server):
    status, data = _post_operation("/divide", {"a": 10, "b": 2})
    assert status == 200
    assert data["result"] == 5


def test_divide_by_zero_api(fastapi_server):
    status, data = _post_operation("/divide", {"a": 10, "b": 0})
    assert status == 400
    assert "error" in data
    assert "Cannot divide by zero!" in data["error"]
