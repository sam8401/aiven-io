from literals import KAFKA_HOST, CA_FILE, CERT_FILE, KEY_FILE, TOPIC
from producer import Producer
from consumer import Consumer


from kafka.admin import NewTopic
from kafka import KafkaAdminClient


def main():
    # Create Kafka topic
    try:
        admin = KafkaAdminClient(bootstrap_servers=kafka_host, 
            security_protocol="SSL",
            ssl_cafile=CA_FILE,
            ssl_certfile=CERT_FILE,
            ssl_keyfile=KEY_FILE
            )

        topic = NewTopic(name=TOPIC,
                         num_partitions=1,
                         replication_factor=1)
        admin.create_topics([topic])
    except Exception:
        pass

    tasks = [
        Producer(),
        Consumer()
    ]

    # Start threads of a publisher/producer and a subscriber/consumer to Kafka topic
    for t in tasks:
        t.start()

    time.sleep(10)

    # Stop threads
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()