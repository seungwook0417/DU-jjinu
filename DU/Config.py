import json


def get_config():
    return json.load(open("config.json"))

def get_hakgwa():
    return json.load(open("hakgwa.json", 'r', encoding="utf-8"))