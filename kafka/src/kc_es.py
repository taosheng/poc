#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
BROKERS_LIST = ['localhost:9092'] 
TOPIC = "my-topic"


from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
def readKafka():
    consumer = KafkaConsumer(TOPIC,
#                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print("usage: python kc_es.py <topic> ")
        exit(0)

    TOPIC = sys.argv[1]
    readKafka()
    