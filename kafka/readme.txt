
1. installation
    1.1 follow this -> https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-14-04
    1.2 install kafka-python client
        https://github.com/dpkp/kafka-python


2. the POC plan
    * a few json text file
    * a simple producer to read one json file to kafka
       * js_kp.py <topic> <json_lines>
         - Json string to kafka producer

    * a simple consumer to read from kafka and indexing in elasticsearch
       * kc_es.py <topic> 
         - kafka Consumer to Elasticsearch

3. Run the POC
    * Requirement
        (1) an Ubuntu 14 server install kafka, elasticsearch, python3
        (2) this git clone
        (3) two terminal ssh to your ubuntu, assume there are Term-1 and Term-2

    * Steps
        1. config: modify a bit of kc_es.py, change elasticsearch IP
           
        2. (Term-1) run consumer: #python3 kc_es.py test1 
      
        3. (Term-2) run producer #python3 js_kp.py test1 demo.txt
 
        4. (Term-1) you can see consumer receive the producer's data
    
        5. (Term-2) check your own elasticsearch server (index name: test-index)
