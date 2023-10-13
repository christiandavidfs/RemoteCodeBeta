# connection_manager.py
import requests
import json

def connect_to_api(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {str(e)}")
        return None

def parse_response(response):
    try:
        api_response = response.json()
        results = api_response.get("results", [])
        return results
    except (json.JSONDecodeError, IndexError):
        print("Error parsing API response.")
        return None
