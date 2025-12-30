# IoT Sensor Data System

## How to run
1. Build Docker image:
   ```powershell
   docker build -t iot-sensor-system .
   
   docker run -p 27017:27017 iot-sensor-system
