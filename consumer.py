#!/usr/bin/env python

# source -> https://github.com/dpkp/kafka-python/blob/master/example.py
import threading, time
from kafka import KafkaConsumer
from literals import KAFKA_HOST, CA_FILE, CERT_FILE, KEY_FILE, TOPIC


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=kafka_host, 
            security_protocol="SSL",
            ssl_cafile=CA_FILE,
            ssl_certfile=CERT_FILE,
            ssl_keyfile=KEY_FILE,
            auto_offset_reset='earliest',
            consumer_timeout_ms=1000)

        consumer.subscribe([TOPIC])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)

                #TODO: Suman: call pg_client.insert_row()
                # here possibly after "decoding" the row from message

                if self.stop_event.is_set():
                    break

        consumer.close()