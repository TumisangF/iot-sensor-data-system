# IoT Sensor Data System

## 📊 Project Overview

This project implements a containerized data processing system for storing and managing environmental IoT sensor data. The system is designed to support large-scale data ingestion, future extensibility of sensor metrics, and portability across different environments.

The prototype uses MongoDB as the database solution and Python for batch-based data ingestion. Docker is used to fully containerize the system and minimize local dependencies.

![IoT](https://www.cyberdb.co/wp-content/uploads/2022/12/iot.jpg)

## 🎯 System Overview

- **Database**: MongoDB (document-oriented, schema-less)
- **Ingestion**: Python-based batch processing
- **Containerization**: Docker
- **Data Source**: Environmental sensor dataset (CSV format)
  
The system supports evolving sensor data structures, allowing additional metrics such as CO₂, noise levels, or fine dust to be stored without schema changes.

### Key Deliverables
1. Install the database solution chosen in the conception phase. To minimize the dependencies of the
local system, install Docker, load an open-source container containing an instance of the MongoDB from Docker Hub and run this container.
2. Write a script to set up the database within that container as needed to fulfill the project requirements.
3. Write a Python script to connect to the database and load the sample data into it.
4. Create a Dockerfile to include all required steps to automate the entire process. This will allow
the data system to be portable to other environments, like another machine, possibly with another operating
system or the cloud.
5. Set up an open GitHub repository to store the code in a version-controlled way.
6. Load the Dockerfile and all associated files needed to run the container into the GitHub repository. Cloning
this repository, it should be possible to run the container that automatically loads the sample data
into the chosen database.

## 📁 Project Structure

```
iot-seonsor-data-system/
│
├── data/
│   └── sensor_data.csv/              # Sample IoT senso dataset from Kaggle
│
├── scripts/
|   ├── init_db.js                    # MangoDB Initialization script
│   └── load_data.py                  # Python batch ingestion script
│
├── Dockerfile                        # Automated system setup
│
├── README.md                   
└── requirements.txt                  # Python dependencies
```

## 🚀 Getting Started

### **Prerequisites**
- Docker installed on the machine

### **Build the Docker Image**
Run the following command from the root directory of the project
```bash
docker build -t iot-sensor-system
```
This will:
1. Start MongoDB instance
2. Initialize the database and collection
3. Load the sensor data into MongoDB in batches

### **Run the container**
Start the container using
```bash
docker run -p 27017:27017 iot-sensor-system
```
## Accessing the Database

### **MongoDB runs on**
```bash
mongodb://localhost:27017
```
### **Database name:**
```bash
environment_db
```
### **Collection name:**
```bash
sensor_readings
```
## Extensibility
The system supports future sensor metrics without requiring schema changes. New measurements such as CO₂, noise levels, or particulate matter can be added as additional fields in the incoming data and will be stored automatically.

## Version Control
All source code, configuration files, and data required to run the system are stored in a public GitHub repository. Cloning the repository and running the Docker commands above is sufficient to deploy the system on any compatible environment.

## 📄 License

This project is for academic and educational purposes. The Titanic dataset is publicly available and commonly used for data science education.

## 👥 Acknowledgments

- **Dataset Source**: Seaborn/Seaborn GitHub
- **Methodology**: Based on principles from Wickham, Tufte, and Cleveland
- **Academic Framework**: Structured around data science best practices

---

**Project Status**: Complete  
**Last Updated**: December 2024  
**Dataset Shape**: 891 passengers × 20 features  
**Data Quality Score**: 95/100 (Comprehensive cleaning applied)
