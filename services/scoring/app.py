import json

def lambda_handler(event, context):
    # scoring lambda triggered by events - simple stub that sums points
    results = event.get("results", [])
    total = sum(r.get("points", 0) for r in results)
    return {"statusCode": 200, "body": json.dumps({"total_points": total})}
