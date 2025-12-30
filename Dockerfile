# Base image: official MongoDB (open-source)
FROM mongo:6.0

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory inside container
WORKDIR /app

# Copy data and scripts
COPY data /app/data
COPY scripts /app/scripts
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy MongoDB initialization script
COPY scripts/init_db.js /docker-entrypoint-initdb.d/

# Start MongoDB, wait briefly, then load data
CMD mongod --fork --logpath /var/log/mongodb.log \
    && sleep 5 \
    && python3 /app/scripts/load_data.py \
    && tail -f /dev/null
