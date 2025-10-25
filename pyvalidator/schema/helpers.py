import json
import base64

def _extract_body_from_event(event):
    # If event is already a dict of user fields, return it as-is
    if not isinstance(event, dict):
        return event

    # API Gateway v1/v2 support
    if "body" in event:
        body = event["body"]
        if body is None:
            return {}
        if event.get("isBase64Encoded"):
            try:
                body = base64.b64decode(body).decode("utf-8")
            except Exception:
                pass
        if isinstance(body, str):
            body = body.strip()
            # Try JSON parse
            try:
                return json.loads(body)
            except Exception:
                # Not JSON, return raw body as a single field if desired
                return {"_raw": body}
        if isinstance(body, dict):
            return body

    # SNS, SQS and other events often place the payload within Records
    if "Records" in event and isinstance(event["Records"], list) and event["Records"]:
        # Return first record body parsed if possible
        rec = event["Records"][0]
        msg = rec.get("body") or rec.get("Sns", {}).get("Message")
        if msg:
            try:
                return json.loads(msg)
            except Exception:
                return {"_raw": msg}

    # Otherwise assume it's already the payload dict
    return event
