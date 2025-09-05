from mmt.athlete.athlete import Athlete

def test_athlete_to_item():
    athlete = Athlete("001", "João Silva", "1990-01-01", "M")
    item = athlete.to_item()
    assert item["PK"] == "ATH#001"
    assert item["SK"] == "METADATA"
    assert item["Tipo"] == "Athlete"
    assert item["Nome"] == "João Silva"
    assert item["DataNascimento"] == "1990-01-01"
    assert item["Sexo"] == "M"
    assert item["Deleted"] is False
