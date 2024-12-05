from prometheus_client import start_http_server, Counter
from kafka import KafkaProducer
import time
import json
import random

# Prometheus Counter for produced messages
produced_messages = Counter('produced_messages', 'Number of messages produced')

# Start Prometheus metrics server on port 9101
start_http_server(9101)

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producer is running...")

while True:
    # Generate random sensor data
    message = {
        "sensor_id": random.randint(1, 5),
        "value": random.uniform(20.0, 30.0),
        "timestamp": time.time()
    }
    # Send data to Kafka topic
    producer.send('sensor-data', message)
    produced_messages.inc()  # Increment Prometheus counter
    print(f"Produced: {message}")
    time.sleep(1);

