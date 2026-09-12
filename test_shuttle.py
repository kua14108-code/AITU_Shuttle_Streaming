import pytest

from shuttle_data import validate_event
from shuttle_api import get_occupancy_category


def test_valid_event():
    event = {
        "Timestamp": "08:01",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 22,
        "Speed_kmh": 28,
        "Status": "ON_ROUTE",
    }

    result = validate_event(event)

    assert result["Passengers"] == 22
    assert result["Status"] == "ON_ROUTE"


def test_negative_passengers():
    event = {
        "Timestamp": "08:01",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": -1,
        "Speed_kmh": 28,
        "Status": "ON_ROUTE",
    }

    with pytest.raises(ValueError):
        validate_event(event)


def test_invalid_speed():
    event = {
        "Timestamp": "08:01",
        "Vehicle_ID": "AITU-Campus",
        "Location": "Residence B02",
        "Passengers": 22,
        "Speed_kmh": 150,
        "Status": "ON_ROUTE",
    }

    with pytest.raises(ValueError):
        validate_event(event)


def test_occupancy_category():
    assert get_occupancy_category(10) == "LOW"
    assert get_occupancy_category(20) == "MEDIUM"
    assert get_occupancy_category(25) == "HIGH"
    assert get_occupancy_category(31) == "OVER_CAPACITY"