import os
import boto3
import json
from datetime import datetime
from boto3.dynamodb.conditions import Key

from mmt.athlete.athlete import Athlete

DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE", "mmt-dev")
dynamodb = boto3.resource("dynamodb", region_name=os.environ.get("AWS_REGION", "us-east-2"))
table = dynamodb.Table(DYNAMODB_TABLE)


def create_athlete(athlete_id, nome, data_nascimento, sexo):
    athlete = Athlete(athlete_id, nome, data_nascimento, sexo)
    table.put_item(Item=athlete.to_item())
    return athlete


def get_athlete(athlete_id):
    response = table.get_item(Key={"PK": f"ATH#{athlete_id}", "SK": "METADATA"})
    item = response.get("Item")
    if item and not item.get("Deleted", False):
        return Athlete.from_item(item)
    return None


def update_athlete(athlete_id, nome=None, data_nascimento=None, sexo=None):
    athlete = get_athlete(athlete_id)
    if not athlete:
        return None
    if nome:
        athlete.nome = nome
    if data_nascimento:
        athlete.data_nascimento = data_nascimento
    if sexo:
        athlete.sexo = sexo
    table.put_item(Item=athlete.to_item())
    return athlete


def delete_athlete(athlete_id):
    athlete = get_athlete(athlete_id)
    if not athlete:
        return None
    athlete.deleted = True
    table.put_item(Item=athlete.to_item())
    return athlete


# Lambda handler
def lambda_handler(event, context):
    action = event.get("action")
    athlete_id = event.get("athlete_id")
    nome = event.get("nome")
    data_nascimento = event.get("data_nascimento")
    sexo = event.get("sexo")

    if action == "create":
        athlete = create_athlete(athlete_id, nome, data_nascimento, sexo)
        return {"result": athlete.to_item()}
    elif action == "get":
        athlete = get_athlete(athlete_id)
        return {"result": athlete.to_item() if athlete else None}
    elif action == "update":
        athlete = update_athlete(athlete_id, nome, data_nascimento, sexo)
        return {"result": athlete.to_item() if athlete else None}
    elif action == "delete":
        athlete = delete_athlete(athlete_id)
        return {"result": athlete.to_item() if athlete else None}
    else:
        return {"error": "Invalid action"}


