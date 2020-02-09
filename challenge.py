#! /usr/bin/env python3
import requests
RAINFOREST_CHALLENGE_URL = "https://letsrevolutionizetesting.com/challenge.json"

def get_request_data(id=None):
    payload = {"id": id}
    data = requests.get(RAINFOREST_CHALLENGE_URL, payload).json()
    print(data)

    if "follow" in data:
        id = data["follow"].split("=")
        get_request_data(id)


if __name__ == "__main__":
    get_request_data()
