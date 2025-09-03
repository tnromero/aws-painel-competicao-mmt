from services.modality import app


def test_list():
    resp = app.lambda_handler({}, None)
    assert resp["statusCode"] == 200


def test_create():
    resp = app.lambda_handler({"action": "create", "body": {"name": "Modal1"}}, None)
    assert resp["statusCode"] == 201
    assert "Modal1" in resp["body"]
