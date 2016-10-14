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
    result  = []
    with open(f) as jsonLines:
        for l in jsonLines.readlines():
            if l.strip() == '':
                continue
            oneJson = json.loads(l)
            result.append(oneJson)
 
    return result

    
def sendToKafka(jsonList):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    #producer = KafkaProducer(bootstrap_servers='localhost:9092')
#    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    #producer = KafkaProducer(key_serializer=str.encode)
    #producer.send(TOPIC, key='foo123123123', value=b'bar111111111')
    for j in jsonList:
        producer.send(TOPIC,j)
    producer.flush()

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print("usage: python js_kp.py <topic> <json file> ")
        exit(0)

    TOPIC = sys.argv[1]
    jsonList = readJsonToDict(sys.argv[2])
    sendToKafka(jsonList)
    
