import json

from shuttle_data import RAW_EVENTS


def create_json_sample(filename: str = "events.json"):
    """Save the shuttle events as a JSON sample."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(RAW_EVENTS, file, indent=4)


if __name__ == "__main__":
    create_json_sample()
    print("JSON sample created: events.json")