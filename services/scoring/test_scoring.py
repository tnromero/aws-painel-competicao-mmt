from services.scoring import app


def test_scoring_empty():
    resp = app.lambda_handler({}, None)
    assert resp["statusCode"] == 200
    assert "total_points" in resp["body"]


def test_scoring_total():
    resp = app.lambda_handler({"results": [{"points": 10}, {"points": 15}]}, None)
    assert resp["statusCode"] == 200
    assert "25" in resp["body"]
