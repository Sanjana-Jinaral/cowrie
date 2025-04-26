import json
from collections import defaultdict

log_path = "/home/kali/cowrie/var/log/cowrie/cowrie.json"  # Adjust path as needed

failed_logins = defaultdict(int)
success_logins = []

with open(log_path, 'r') as f:
    for line in f:
        try:
            log = json.loads(line)
            if log.get("eventid") == "cowrie.login.failed":
                failed_logins[log.get("src_ip")] += 1
            elif log.get("eventid") == "cowrie.login.success":
                success_logins.append((log.get("src_ip"), log.get("username")))
        except:
            continue

for ip, count in failed_logins.items():
    if count > 5:
        print(f"[!] Suspicious IP: {ip} with {count} failed login attempts")

print("\n[+] Successful Logins:")
for ip, user in success_logins:
    print(f"{ip} -> {user}")
