#!/usr/bin/env python
# source -> https://github.com/dpkp/kafka-python/blob/master/example.py
import threading, time
from kafka import KafkaProducer
from literals import KAFKA_HOST, CA_FILE, CERT_FILE, KEY_FILE, TOPIC


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=kafka_host, 
            security_protocol="SSL",
            ssl_cafile=CA_FILE,
            ssl_certfile=CERT_FILE,
            ssl_keyfile=KEY_FILE
            )

    
        while not self.stop_event.is_set():

            # Suman: TODO: Call website_checker.check() here and pass the dict result to consumer

            producer.send(TOPIC, b"test")
            time.sleep(1)

        producer.close()



