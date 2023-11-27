import json

data = {
    "name": None,
    "location": None,
    "inventory": {
        "hotbar": [None , None , None],
        "equipped": [None , None , None, None],
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
    },
    "achivement": []
}

def save_data(data):
    try:
        with open("data/player.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(data)

    with open("data/player.json", "w") as data_file:
        json.dump(existing_data, data_file)

def load_data():
    with open("data/player.json") as data_file:
        return json.load(data_file)

