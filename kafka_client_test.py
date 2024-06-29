import json
import logging
import time
import threading

from confluent_kafka import Producer, Consumer
import faker


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

server = 'localhost:30000'

config: dict = {
    'producer': {
        'bootstrap.servers': server,
        'acks':              'all'
    },
    'consumer': {
        'bootstrap.servers': server,
        'group.id':          'kafka-kubernetes-group',
        'auto.offset.reset': 'earliest'
    }
}


def generate_profile() -> dict:
    fake = faker.Faker()

    return {
        'id': fake.passport_number(),
        'name': fake.name(),
        'address': fake.address(),
    }


def on_delivery_cb(err, msg):
    if err:
        logger.error(f'ERROR: Message failed delivery: {err}')
    else:
        logger.info("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


def produce(topic: str) -> None:
    msg_count = 0
    logger.info('about to start producing messages')

    producer = Producer(config['producer'])

    try:
        while True: # produce forever :)
            profile = generate_profile()
            key: str = profile.get('id')
            value: str = json.dumps(profile)

            producer.produce(topic, value, key, callback=on_delivery_cb)

            if msg_count % 500 == 0:
                res = producer.poll(10)
                logger.info(f'{res} messages polled')
            
            time.sleep(0.1)
            msg_count += 1
    except Exception as e:
        logger.info(e)
    finally:
        producer.flush()
        logger.info(f'{msg_count} messages sent')


def consume(topic: str) -> None:
    msg_count = 0
    logger.info('about to start consuming messages')

    consumer = Consumer(config['consumer'])
    consumer.subscribe([topic])

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                msg_count += 1

                # Extract the (optional) key and value, and print.
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        logger.info(f'{msg_count} messages consumed')
        consumer.close()


if __name__ == '__main__':
    topic = 'hello-topic'
    
    c = threading.Thread(target=consume, args=(topic,))
    c.start()
    
    p = threading.Thread(target=produce, args=(topic,))
    p.start()
