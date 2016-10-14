#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError
BROKERS_LIST = ['localhost:9092'] 
TOPIC = "my-topic"

def readJsonToDict(f):
    result = {'test_004':'value_004'}
    return result

    
def sendToKafka(jsonDict):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    #producer = KafkaProducer(bootstrap_servers='localhost:9092')
#    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    #producer = KafkaProducer(key_serializer=str.encode)
    #producer.send(TOPIC, key='foo123123123', value=b'bar111111111')
    producer.send(TOPIC,jsonDict)
    producer.flush()

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print("usage: python js_kp.py <topic> <json file> ")
        exit(0)

    TOPIC = sys.argv[1]
    jsonDict = readJsonToDict(sys.argv[2])
    sendToKafka(jsonDict)
    
