from fastapi import FastAPI
from pydantic import BaseModel, Field

from shuttle_data import validate_event


app = FastAPI(
    title="AITU Campus Shuttle API",
    description="API for validating campus shuttle streaming events",
    version="1.0.0",
)


class ShuttleEvent(BaseModel):
    Timestamp: str
    Vehicle_ID: str
    Location: str
    Passengers: int = Field(ge=0)
    Speed_kmh: float = Field(ge=0, le=120)
    Status: str


def get_occupancy_category(passengers: int) -> str:
    """Return an occupancy category based on passenger count."""

    if passengers <= 10:
        return "LOW"
    if passengers <= 20:
        return "MEDIUM"
    if passengers <= 30:
        return "HIGH"
    return "OVER_CAPACITY"


@app.post("/events")
def receive_event(event: ShuttleEvent):
    """Validate and classify one incoming shuttle event."""

    raw_event = event.model_dump()

    try:
        validated_event = validate_event(raw_event)

        return {
            "status": "accepted",
            "errors": [],
            "occupancy_category": get_occupancy_category(
                validated_event["Passengers"]
            ),
        }

    except (ValueError, TypeError) as error:
        return {
            "status": "rejected",
            "errors": [str(error)],
            "occupancy_category": None,
        }