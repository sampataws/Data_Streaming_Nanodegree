import asyncio
from datetime import  datetime

from confluent_kafka import Consumer,Producer
from confluent_kafka.admin import AdminClient,NewTopic


BROKER_URL = "PLAINTEXT://localhost:9092"

async def produce(topic_name):
    """Produces data into the Kafka Topic"""
    #
    #TODO: Try running the producer with the basic settings and then tweaking the configuration
    #

    p = Producer({
        "bootstrap.servers":BROKER_URL
        #"linger.ms":"",
        #"batch.num.messages":"",
        #"queue.buffering.max.messages":"",
        #"queue.buffering.max.kbytes":""
    })

    start_time = datetime.utcnow()
    curr_iteration = 0
    while True:
        p.produce(topic_name,f"iteration: {curr_iteration}")
        if curr_iteration % 100:
            elapsed = (datetime.utcnow() - start_time).seconds
            print(f"Messages Sent: {curr_iteration} | Total elapsed seconds: {elapsed} " )
        curr_iteration += 1

        # We call poll here to flush message delivery reports from Kafka
        # We don't care about the details, so calling it with a timeout of 0s
        # means it returns immediately and has very little performance impact.
        p.poll(0)

async def consume(topic_name):
    """Consumes data from Kafka Topic"""
    c = Consumer({
        "bootstrap.servers": BROKER_URL,
        "group.id":"0"
    })

    c.subscribe([topic_name])
    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(1)

def main():
    """Runs the exercise"""
    # TODO: Configure the AdminClient with `bootstrap.servers`
    #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.admin.AdminClient
    client = AdminClient({"bootstrap.servers": BROKER_URL})

    try:
        asyncio.run(produce_consume("com.udacity.lesson2.sample4.purchases"))
    except KeyboardInterrupt as e:
        print("shutting down")


async def produce_consume(topic_name):
    """Runs the Produces and Consumer tasks"""
    t1 = asyncio.create_task(produce(topic_name))
    t2 = asyncio.create_task(consume(topic_name))
    await t1
    await t2

if __name__ == "__main__":
    main()


