# source -> https://github.com/dpkp/kafka-python/blob/master/example.py

import json
import threading, time

from kafka import KafkaProducer
from literals import KAFKA_HOST, CA_FILE, CERT_FILE, KEY_FILE, TOPIC
from literals import WEBSITE as website, WEBSITE_TITLE as title
from website_checker import check

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=KAFKA_HOST, 
            security_protocol="SSL",
            ssl_cafile=CA_FILE,
            ssl_certfile=CERT_FILE,
            ssl_keyfile=KEY_FILE,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )

    
        while not self.stop_event.is_set():

            metrics = check(website, title)
            producer.send(TOPIC, metrics)
            
            time.sleep(1)

        producer.close()



