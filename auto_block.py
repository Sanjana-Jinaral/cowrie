import json
import os
from collections import defaultdict

# Path to the log file
log_path = "/home/kali/cowrie/var/log/cowrie/cowrie.json"

# Dictionary to count failed login attempts by IP
ips = defaultdict(int)

# Debugging: Print log file path
print(f"Opening log file at: {log_path}")

# Flag to check if we found any failed login events
found_failed_logins = False

# Open and process the log file
with open(log_path) as f:
    for line in f:
        try:
            # Load each line as a JSON object
            log = json.loads(line)
            print(f"Processing log entry: {log}")  # Debug print
            
            # Check for failed login event
            if log.get("eventid") == "cowrie.login.failed":
                src_ip = log.get("src_ip")
                if src_ip:
                    ips[src_ip] += 1
                    found_failed_logins = True  # Mark that we found a failed login event
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

# Handle case where no failed login attempts were found
if not found_failed_logins:
    print("[*] No failed login events found, continuing with the script...")

# Process and block IPs with too many failed attempts
for ip, count in ips.items():
    print(f"IP: {ip} | Failed Login Attempts: {count}")
    if count > 10:
        print(f"Blocking {ip} with {count} failed login attempts")
        os.system(f"sudo ufw deny from {ip}")

# Final message
print("[*] Script completed.")

