from datetime import datetime
from typing import Generator


RAW_EVENTS = [
    {
        "Timestamp": "08:00",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B01",
        "Passengers": 18,
        "Speed_kmh": 31,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:01",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 22,
        "Speed_kmh": 28,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:02",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B01",
        "Passengers": 21,
        "Speed_kmh": 29,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:03",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 25,
        "Speed_kmh": 27,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:04",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B01",
        "Passengers": 24,
        "Speed_kmh": 0,
        "Status": "STOPPED",
    },
    {
        "Timestamp": "08:05",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 26,
        "Speed_kmh": 30,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:06",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B01",
        "Passengers": 23,
        "Speed_kmh": 32,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:07",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 28,
        "Speed_kmh": 26,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:08",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B01",
        "Passengers": 27,
        "Speed_kmh": 25,
        "Status": "ON_ROUTE",
    },
    {
        "Timestamp": "08:09",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 30,
        "Speed_kmh": 24,
        "Status": "ON_ROUTE",
    },
]


def _parse_timestamp(timestamp: str):
    """Convert HH:MM timestamp into a time object."""
    return datetime.strptime(timestamp, "%H:%M").time()


def validate_event(raw_event: dict) -> dict:
    """Validate one shuttle event and return the cleaned event."""

    event = raw_event.copy()

    event["Timestamp"] = _parse_timestamp(event["Timestamp"])

    if not isinstance(event["Passengers"], int) or event["Passengers"] < 0:
        raise ValueError("Passengers must be a non-negative integer.")

    if not isinstance(event["Speed_kmh"], (int, float)):
        raise ValueError("Speed_kmh must be a number.")

    if not 0 <= event["Speed_kmh"] <= 120:
        raise ValueError("Speed_kmh must be between 0 and 120 km/h.")

    if event["Status"] not in {"ON_ROUTE", "STOPPED"}:
        raise ValueError("Status must be ON_ROUTE or STOPPED.")

    return event


def event_generator() -> Generator[dict, None, None]:
    """Yield validated shuttle events one at a time."""

    for raw_event in RAW_EVENTS:
        yield validate_event(raw_event)


if __name__ == "__main__":
    for event in event_generator():
        print("OK:", event)