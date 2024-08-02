import json
from airflow.models import Variable
from utils.kafka_producer import get_kafka_producer

KAFKA_BOOTSTRAP_SERVERS = 'server01:9092,server02:9092,server03:9092'
KAFKA_TOPIC = 'car_info'

def send_to_kafka(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='fetch_and_update_address')
    if not isinstance(data, list):
        raise ValueError(f"Expected list from fetch_and_update_address, but got: {type(data)}")

    producer = get_kafka_producer(KAFKA_BOOTSTRAP_SERVERS)
    for item in data:
        producer.send(KAFKA_TOPIC, item)
    producer.flush()
