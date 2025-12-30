import pandas as pd
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "environment_db"
COLLECTION_NAME = "sensor_readings"
BATCH_SIZE = 1000


def main():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Load CSV data
    df = pd.read_csv("/app/data/sensor_data.csv")

    # Convert DataFrame to list of dictionaries
    records = df.to_dict(orient="records")

    # Insert data in batches
    for i in range(0, len(records), BATCH_SIZE):
        batch = records[i:i + BATCH_SIZE]
        collection.insert_many(batch)
        print(f"Inserted records {i} to {i + len(batch)}")

    print("Data ingestion completed successfully.")


if __name__ == "__main__":
    main()
