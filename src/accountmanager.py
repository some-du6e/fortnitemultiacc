import os
import shutil
import sys
import json
import requests

def isnewuser():
    def isnewuser():
        config_path = os.path.expanduser('~/.config/fnmanager/config.json')

        if not os.path.exists(config_path):
            return True  # File does not exist, user is new

        try:
            with open(config_path, 'r') as config_file:
                config_data = json.load(config_file)
                return not config_data.get('isnewuser', False)
        except json.JSONDecodeError:
            return True  # Malformed JSON, treat as new user
        except Exception as e:
            print(f"An error occurred: {e}")
            return True  # Any other error, treat as new user



def initialize():
    if isnewuser():
        shutil.copy("config.example.json","config.json")

def get_config():
    initialize()
    return json.load(open("config.json"))


def get_accounts():
    accounts = []
    for i in os.listdir(os.path.expanduser('~/.config/fnmanager/accounts')):
        with open(os.path.expanduser(f'~/.config/fnmanager/accounts/{i}')) as f:
            accounts.append(json.load(f))
    return accounts

def get_account_xp(account_name):
    parameters = {
        "name": account_name
    }
    headers = {
        'Authorization': get_config().get("fortnite-api-key"),
        'Content-Type': 'application/json'
    }
    url = "https://fortnite-api.com/v2/stats/br/v2"
    response = requests.get(url, params=parameters, headers=headers)
    level = response.json().get("data", {}).get("battlePass", {}).get("level", 0)
    return level
