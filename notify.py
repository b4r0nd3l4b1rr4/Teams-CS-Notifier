#!/usr/bin/env python3

# notify.py
import requests
import json
import base64
import sys

def send_teams_notification(title, external_ip, internal_ip, hostname, username):

    webhook_url = "WEBHOOK_HERE"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "title": title,
        "text": "New Beacon notification",
        "sections": [
            {
                "facts": [
                    {
                        "name": "New Beacon from:",
                        "value": external_ip
                    },
                    {
                        "name": "Internal_IP:",
                        "value": internal_ip
                    },
                    {
                        "name": "Host.name:",
                        "value": hostname
                    },
                    {
                        "name": "User.name:",
                        "value": username
                    }
                ]
            }
        ]
    }
    try:
        json.loads(json.dumps(payload))
    except ValueError as e:
        print(f"Invalid JSON: {e}")

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    #print(response.status_code)
    return response.status_code

if __name__ == "__main__":
    title = sys.argv[1]
    external_ip = sys.argv[2].split(':')[1].strip()
    internal_ip = sys.argv[3].split(':')[1].strip()
    hostname = sys.argv[4].split(':')[1].strip()
    username = sys.argv[5].split(':')[1].strip()
    
    
    send_teams_notification(title, external_ip, internal_ip, hostname, username)
