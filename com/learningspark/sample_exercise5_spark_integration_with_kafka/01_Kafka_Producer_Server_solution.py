"""Exercise - Create a Kafka Producer Server
In this workspace, you’re going to create a Kafka Producer Server.
You’ll be using this code for the next few workspace exercises.
You have already learned how to create a Kafka Producer Server in the previous Kafka course,
so refer back to those lessons if you need to! We’re just starting you with an empty Python file for this exercise,
 but you can refer to the solution code if you really need to. (Try not to!)

Requirements:

* Your Kafka Server should ingest the uber.json data file in the workspace correctly. If unsure of the correct path of the file, type pwd in the console to get the absolute path of the file.
* You can name your own topic and feel free to use any free port number for this server.
* This will be your bootstrap server for your streaming application.
* You should be able to check if your server ingests data correctly by using Kafka Consumer Console.
* You can use any Kafka library (pykafka, kafka, kafka-confluent, etc). \
   But if you wish to use a library other than kafka-confluent or kafka-python, \
   you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up,
   or reset data, or used the "Get New Content" button). \
   The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.
"""

from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file) as f:
            for line in f:
                message = self.dict_to_binary(line)
                self.send(self.topic, message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')