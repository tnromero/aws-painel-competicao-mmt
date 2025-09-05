from mmt.result import app


def test_list():
    resp = app.lambda_handler({}, None)
    assert resp["statusCode"] == 200


def test_create():
    resp = app.lambda_handler({"action": "create", "body": {"score": 100}}, None)
    assert resp["statusCode"] == 201
    assert "100" in resp["body"]
