import pytest
from unittest.mock import patch, MagicMock
from mmt.athlete import lambda_function

@pytest.fixture
def athlete_data():
    return {
        "athlete_id": "001",
        "nome": "João Silva",
        "data_nascimento": "1990-01-01",
        "sexo": "M"
    }

def test_create_athlete(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.put_item = MagicMock()
        athlete = lambda_function.create_athlete(**athlete_data)
        item = athlete.to_item()
        assert item["PK"] == "ATH#001"
        assert item["SK"] == "METADATA"
        assert item["Tipo"] == "Athlete"
        assert item["Nome"] == "João Silva"
        assert item["DataNascimento"] == "1990-01-01"
        assert item["Sexo"] == "M"
        assert item["Deleted"] is False

def test_get_athlete(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        athlete = lambda_function.get_athlete(athlete_data["athlete_id"])
        assert athlete is not None
        assert athlete.nome == "João Silva"
        assert athlete.data_nascimento == "1990-01-01"
        assert athlete.sexo == "M"
        assert athlete.deleted is False

def test_update_athlete(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        mock_table.put_item = MagicMock()
        athlete = lambda_function.update_athlete(athlete_data["athlete_id"], nome="Maria", data_nascimento="1992-02-02", sexo="F")
        assert athlete.nome == "Maria"
        assert athlete.data_nascimento == "1992-02-02"
        assert athlete.sexo == "F"

def test_delete_athlete(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        mock_table.put_item = MagicMock()
        athlete = lambda_function.delete_athlete(athlete_data["athlete_id"])
        assert athlete.deleted is True

def test_lambda_handler_create(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.put_item = MagicMock()
        event = {"action": "create", **athlete_data}
        result = lambda_function.lambda_handler(event, None)
        assert result["result"]["PK"] == "ATH#001"
        assert result["result"]["Nome"] == "João Silva"

def test_lambda_handler_get(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        event = {"action": "get", "athlete_id": "001"}
        result = lambda_function.lambda_handler(event, None)
        assert result["result"]["PK"] == "ATH#001"
        assert result["result"]["Nome"] == "João Silva"

def test_lambda_handler_update(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        mock_table.put_item = MagicMock()
        event = {"action": "update", "athlete_id": "001", "nome": "Maria", "data_nascimento": "1992-02-02", "sexo": "F"}
        result = lambda_function.lambda_handler(event, None)
        assert result["result"]["Nome"] == "Maria"
        assert result["result"]["DataNascimento"] == "1992-02-02"
        assert result["result"]["Sexo"] == "F"

def test_lambda_handler_delete(athlete_data):
    with patch.object(lambda_function, "table") as mock_table:
        mock_table.get_item = MagicMock(return_value={"Item": lambda_function.Athlete(**athlete_data).to_item()})
        mock_table.put_item = MagicMock()
        event = {"action": "delete", "athlete_id": "001"}
        result = lambda_function.lambda_handler(event, None)
        assert result["result"]["Deleted"] is True

def test_lambda_handler_invalid():
    event = {"action": "invalid"}
    result = lambda_function.lambda_handler(event, None)
    assert "error" in result
