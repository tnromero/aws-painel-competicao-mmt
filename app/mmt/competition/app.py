import json

def lambda_handler(event, context):
    # Simple create/list stub for competitions
    action = event.get("action", "list")
    if action == "create":
        body = event.get("body", {})
        return {"statusCode": 201, "body": json.dumps({"message": "competition created", "item": body})}
    return {"statusCode": 200, "body": json.dumps({"items": []})}
