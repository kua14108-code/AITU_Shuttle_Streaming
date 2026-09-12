import time

from shuttle_data import event_generator


def simulate_arrival(delay_seconds: float = 1.0):
    """Simulate chronological arrival of shuttle events."""

    for event in event_generator():
        yield event
        if delay_seconds > 0:
            time.sleep(delay_seconds)


def process_stream(delay_seconds: float = 0):
    """Process events one by one without loading the whole stream."""

    processed_events = []

    for event in simulate_arrival(delay_seconds):
        processed_events.append(
            {
                "Timestamp": event["Timestamp"].strftime("%H:%M"),
                "Vehicle_ID": event["Vehicle_ID"],
                "Location": event["Location"],
                "Passengers": event["Passengers"],
                "Speed_kmh": event["Speed_kmh"],
                "Status": event["Status"],
                "Processed": "Yes",
            }
        )

    return processed_events


if __name__ == "__main__":
    for event in simulate_arrival(delay_seconds=0):
        print(
            f"{event['Timestamp'].strftime('%H:%M')} | "
            f"{event['Vehicle_ID']} | "
            f"{event['Location']} | "
            f"{event['Passengers']} passengers | "
            f"{event['Speed_kmh']} km/h | "
            f"{event['Status']}"
        )