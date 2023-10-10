from confluent_kafka import Consumer,KafkaError, KafkaException
import json

conf = {'bootstrap.servers': '172.18.0.3:9092',
        'group.id': 'foo',
        'auto.offset.reset': 'smallest',}

consumer = Consumer(conf)

consumer.subscribe(['events'])


while True:
    msg = consumer.poll(timeout=1.0)

    if msg is None: continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
            raise KafkaException(msg.error())
    else:
        print(msg.value().decode('utf8'))