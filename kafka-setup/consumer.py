from prometheus_client import start_http_server, Counter
from kafka import KafkaConsumer
import json

# Prometheus counter for messages consumed
consumed_messages = Counter('consumed_messages', 'Number of messages consumed')

# Start Prometheus metrics server on port 9103
start_http_server(9103)

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'sensor-data',  # Kafka topic to consume from
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON messages
)

print("Consumer is running...")

for message in consumer:
    # Increment Prometheus metric
    consumed_messages.inc()

    # Process the message
    print(f"Consumed: {message.value}")
