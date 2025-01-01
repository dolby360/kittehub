"""This module demonstrates the usage of AutoKitteh webhooks."""
import requests
import os

BASE_URL = os.getenv("HTTP_WIN_BASE_URL")  # Set in "autokitteh.yaml".

def send_requests(event):
    url = f"{BASE_URL}/webhook"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=event, headers=headers)
    print(response.text)
