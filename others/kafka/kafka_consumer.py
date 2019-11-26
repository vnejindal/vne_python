from kafka import KafkaConsumer, KafkaProducer
from json import loads,dumps
import ssl

sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_PLAINTEXT'
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          value_serializer=lambda x:
#                          dumps(x).encode('utf-8'))
# producer.send('kafka-topic',value='itsme')
try:
    consumer = KafkaConsumer('kafka-topic', bootstrap_servers=['kafka.url.com:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')) , sasl_plain_username = "kafka-user", sasl_plain_password = "kafka-password",sasl_mechanism = sasl_mechanism,security_protocol = security_protocol)
    for message in consumer:
        try:
            print(message.key, message.value)
            #obj = message.value
            #print(obj)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)




