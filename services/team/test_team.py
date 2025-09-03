from services.team import app


def test_list():
    resp = app.lambda_handler({}, None)
    assert resp["statusCode"] == 200


def test_create():
    resp = app.lambda_handler({"action": "create", "body": {"name": "Team1"}}, None)
    assert resp["statusCode"] == 201
    assert "Team1" in resp["body"]
