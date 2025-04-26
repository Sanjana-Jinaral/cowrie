import requests

def send_slack_alert(message):
    webhook_url = "https://hooks.slack.com/services/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  # your URL here
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

# Example usage
send_slack_alert("🚨 Honeypot Alert: New suspicious activity detected!")
