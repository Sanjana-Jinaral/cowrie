import json
import pandas as pd

log_path = "/home/kali/cowrie/var/log/cowrie/cowrie.json"
rows = []

with open(log_path, 'r') as f:
    for line in f:
        try:
            log = json.loads(line)
            if log.get("eventid") in ["cowrie.login.failed", "cowrie.login.success"]:
                rows.append({
                    "ip": log.get("src_ip"),
                    "username": log.get("username"),
                    "event": log.get("eventid"),
                    "timestamp": log.get("timestamp")
                })
        except json.JSONDecodeError:
            continue  # skip malformed lines

# Save to CSV
df = pd.DataFrame(rows)
if not df.empty:
    df.to_csv("cowrie_login_events.csv", index=False)
    print(f"[+] Exported {len(df)} login events to cowrie_login_events.csv")
else:
    print("[-] No login events found.")

