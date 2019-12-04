## Sample Kafka clients at single place - Consumer and Producer
## Fill the fields of kafka variables defined below and get going... 

from kafka import KafkaConsumer, KafkaProducer
from json import loads,dumps
from time import sleep
from time import time
import sys
#import ssl

kafka_topic = 'sample_topic' 
kafka_bootstrap_server = 'kafka_url:9092'
kafka_sasl_username = 'username'
kafka_sasl_password = 'password' 
sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_PLAINTEXT'
timeout = 10

def kafka_producer():
    
    while True:
        ctime = time()
        print "publishing data "
        producer = KafkaProducer(bootstrap_servers=[kafka_bootstrap_server],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'),  sasl_plain_username = kafka_sasl_username, sasl_plain_password = kafka_sasl_password, sasl_mechanism = sasl_mechanism,security_protocol = security_protocol)
        producer.send(kafka_topic, key='value1', value='Hiii')
        sleep(timeout)


def kafka_consumer():
    try:
        consumer = KafkaConsumer(kafka_topic, bootstrap_servers=[kafka_bootstrap_server],
                                 value_deserializer=lambda x: loads(x.decode('utf-8')) , sasl_plain_username = kafka_sasl_username, sasl_plain_password = kafka_sasl_password, sasl_mechanism = sasl_mechanism,security_protocol = security_protocol)
        for message in consumer:
            try:
                print(message.key, message.value)
                #obj = message.value
                #print(obj)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def main(mode):
    print "mode is ", mode
    if mode == 'producer':
        kafka_producer()
    elif mode == 'consumer':
        kafka_consumer()
    else:
        print 'invalid mode', mode

if __name__ == '__main__':
    mode = sys.argv[1]
    main(mode)
