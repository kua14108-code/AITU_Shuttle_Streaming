# AITU Campus Shuttle Streaming

## Project Overview

This project implements a small Python-based streaming system for synthetic AITU campus shuttle data.

The system receives shuttle events containing:

- timestamp;
- vehicle ID;
- location;
- passenger count;
- speed;
- status.

The project demonstrates data validation, generators, JSON conversion, basic analysis and a FastAPI endpoint.

## Project Structure

```text
AITU_Shuttle_Streaming/
│
├── data/
├── tests/
├── .venv/
├── shuttle_data.py
├── shuttle_streaming.py
├── shuttle_api.py
├── shuttle_analysis.py
├── make_json_sample.py
├── test_shuttle.py
├── main.py
├── README.md
└── requirements.txt
```

## Main Files

### `shuttle_data.py`

Contains the synthetic shuttle dataset, event validation and the event generator.

### `shuttle_streaming.py`

Simulates chronological event arrival and processes events one at a time.

### `shuttle_api.py`

Provides the FastAPI `POST /events` endpoint and calculates the occupancy category.

### `shuttle_analysis.py`

Calculates average passengers, maximum passengers, STOPPED events and the busiest event.

### `make_json_sample.py`

Converts the shuttle events into a JSON sample.

### `test_shuttle.py`

Contains automated tests for event validation and occupancy classification.

## Validation Rules

The system validates each shuttle event using the following rules:

- `Timestamp` must use the `HH:MM` format.
- `Passengers` must be a non-negative integer.
- `Speed_kmh` must be between 0 and 120.
- `Status` must be either `ON_ROUTE` or `STOPPED`.

## Occupancy Categories

| Passengers | Category |
|------------|----------|
| 0–10 | LOW |
| 11–20 | MEDIUM |
| 21–30 | HIGH |
| >30 | OVER_CAPACITY |

## How to Run

Activate the virtual environment and run:

```bash
python shuttle_data.py
python shuttle_streaming.py
python make_json_sample.py
python shuttle_analysis.py
pytest -v
```

To start the FastAPI server:

```bash
python -m uvicorn shuttle_api:app --reload
```

Then open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Example API Request

```json
{
  "Timestamp": "08:01",
  "Vehicle_ID": "AITU-Campus",
  "Location": "Residence B02",
  "Passengers": 22,
  "Speed_kmh": 28,
  "Status": "ON_ROUTE"
}
```

Expected result:

```json
{
  "status": "accepted",
  "errors": [],
  "occupancy_category": "HIGH"
}
```

## Testing

The project contains four automated tests covering:

1. Valid event validation.
2. Negative passenger validation.
3. Invalid speed validation.
4. Occupancy category classification.

## Analysis Results

For the provided synthetic dataset:

- Average passengers: `24.4`
- Maximum passengers: `30`
- Number of STOPPED events: `1`
- Busiest minute: `08:09`
- Busiest location: `Residence B02`
- Busiest event passenger count: `30`

## Generator-Based Streaming

The project uses Python generators to process events one at a time.

The `event_generator()` function uses `yield`, which means that events are produced only when they are requested. This approach is more suitable for a potentially unlimited data stream because the whole stream does not need to be loaded into memory at once.

## Limitation

The current dataset uses only `HH:MM` timestamps and assumes chronological arrival.

A possible improvement is to use complete datetime values and support out-of-order events with a small buffering mechanism.

## Conclusion

The project demonstrates the basic principles of processing streaming data with Python.

The events are validated, generated one at a time, converted to JSON, analysed and exposed through a FastAPI endpoint.

The implementation uses generators because they allow events to be processed individually and are suitable for continuous or potentially unlimited streams.