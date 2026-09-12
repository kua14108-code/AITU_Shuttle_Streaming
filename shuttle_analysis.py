from shuttle_data import event_generator


def analyze_events():
    """Calculate basic statistics for the shuttle stream."""

    events = list(event_generator())

    passenger_counts = [event["Passengers"] for event in events]

    average_passengers = sum(passenger_counts) / len(passenger_counts)
    maximum_passengers = max(passenger_counts)

    stopped_events = [
        event for event in events
        if event["Status"] == "STOPPED"
    ]

    busiest_event = max(
        events,
        key=lambda event: event["Passengers"]
    )

    return {
        "average_passengers": average_passengers,
        "maximum_passengers": maximum_passengers,
        "stopped_count": len(stopped_events),
        "busiest_minute": busiest_event["Timestamp"].strftime("%H:%M"),
        "busiest_vehicle": busiest_event["Vehicle_ID"],
        "busiest_location": busiest_event["Location"],
        "busiest_passengers": busiest_event["Passengers"],
    }


if __name__ == "__main__":
    results = analyze_events()

    print("Average passengers:", results["average_passengers"])
    print("Maximum passengers:", results["maximum_passengers"])
    print("Number of STOPPED events:", results["stopped_count"])
    print(
        "Busiest minute:",
        results["busiest_minute"],
        "|",
        results["busiest_vehicle"],
        "|",
        results["busiest_location"],
        "|",
        results["busiest_passengers"],
        "passengers",
    )