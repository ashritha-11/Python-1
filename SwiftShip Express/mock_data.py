"""
Generate mock raw API data for SwiftShip Express ETL
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
import random

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def utc_ts():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def generate_live_deliveries():
    data = []
    base_time = datetime.utcnow()

    for i in range(10):
        dispatch = base_time - timedelta(hours=random.randint(1, 10))

        expected = dispatch + timedelta(hours=random.randint(6, 12))
        actual = (
            expected + timedelta(hours=random.randint(-2, 4))
            if random.random() > 0.3 else None
        )

        data.append({
            "shipment_id": f"SHP{i+1:03d}",
            "source_city": random.choice(["Hyderabad", "Delhi", "Mumbai", "Chennai"]),
            "destination_city": random.choice(["Bangalore", "Pune", "Kolkata", "Ahmedabad"]),
            "dispatch_time": dispatch.isoformat(),
            "expected_delivery_time": expected.isoformat(),
            "actual_delivery_time": actual.isoformat() if actual else None,
            "package_weight": round(random.uniform(1, 10), 2),
            "agent_id": f"AG{1000+i}"
        })

    filename = RAW_DIR / f"live_deliveries_{utc_ts()}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print("Generated:", filename)


def generate_route_traffic():
    cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Pune", "Bangalore"]

    data = []
    for city in cities:
        data.append({
            "city": city,
            "traffic_congestion_score": random.randint(1, 10),
            "avg_speed": random.randint(15, 45),
            "weather_warnings": random.choice(["None", "Rain", "Storm", "High Winds"])
        })

    filename = RAW_DIR / f"route_traffic_{utc_ts()}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print("Generated:", filename)


if __name__ == "__main__":
    print("Generating mock raw data...")
    generate_live_deliveries()
    generate_route_traffic()
    print("Mock data created in data/raw/")
