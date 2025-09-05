from app.competition import app


def test_list():
    resp = app.lambda_handler({}, None)
    assert resp["statusCode"] == 200


def test_create():
    resp = app.lambda_handler({"action": "create", "body": {"name": "Comp1"}}, None)
    assert resp["statusCode"] == 201
    assert "Comp1" in resp["body"]
