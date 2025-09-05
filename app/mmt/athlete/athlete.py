
class Athlete:
    def __init__(self, athlete_id, nome, data_nascimento, sexo, deleted=False):
        self.athlete_id = athlete_id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.deleted = deleted

    def to_item(self):
        return {
            "PK": f"ATH#{self.athlete_id}",
            "SK": "METADATA",
            "Tipo": "Athlete",
            "Nome": self.nome,
            "DataNascimento": self.data_nascimento,
            "Sexo": self.sexo,
            "Deleted": self.deleted
        }

    @staticmethod
    def from_item(item: dict):
        return Athlete(
            athlete_id=item["PK"].replace("ATH#", ""),
            nome=item.get("Nome"),
            data_nascimento=item.get("DataNascimento"),
            sexo=item.get("Sexo"),
            deleted=item.get("Deleted", False)
        )