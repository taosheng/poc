#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime
import time

BROKERS_LIST = ['localhost:9092'] 
ES_HOST = '10.1.192.79'
TOPIC = "my-topic"

#es.indices.refresh(index="testi")

# To consume latest messages and index in es
def consumeKafkaToEs():
    es = Elasticsearch(
        hosts=[{'host': ES_HOST, 'port': 9200}],
        connection_class=RequestsHttpConnection
    )
    print(es.info())
    consumer = KafkaConsumer(TOPIC,
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
#                         value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
    for message in consumer:
        print(dir(message))
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
        toInsert = json.loads(message.value.decode("utf-8") )
        res = es.index(index="test-index", doc_type='fb',  body=toInsert)
        print("done insert")
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print("usage: python kc_es.py <topic> ")
        exit(0)

    TOPIC = sys.argv[1]
    consumeKafkaToEs()
    
