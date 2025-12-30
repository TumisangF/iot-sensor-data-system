// Switch to (or create) the project database
db = db.getSiblingDB("environment_db");

// Create a collection for sensor readings
db.createCollection("sensor_readings");

// Index for time-based queries
db.sensor_readings.createIndex({ ts: 1 });

// Index for device-based queries
db.sensor_readings.createIndex({ device: 1 });
