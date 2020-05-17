import json
import requests


KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "jdbc_source_mysql_posts"


def configure_connector():
    """Calls Kafka Connect to create the Connector"""
    print("creating or updating kafka connect connector...")

    rest_method = requests.post

    resp = requests.get(f"{KAFKA_CONNECT_URL}/{CONNECTOR_NAME}")
    if resp.status_code == 200:
        return


    resp = rest_method(
        KAFKA_CONNECT_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "name": "jdbc_source_mysql_posts-jdbc",  # TODO
                    "config": {
                        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",  # TODO
                        "topic.prefix": "connect-mysql-",  # TODO
                        "mode": "bulk",  # TODO
                        "table.whitelist": "posts",  # TODO
                        "tasks.max": 1,
                        "connection.url": "jdbc:mysql://localhost:3306/simpplr?user=root&password=password",
                        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                        "key.converter.schemas.enable": "false",
                        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                        "value.converter.schemas.enable": "false",
                },

            }
        ),
    )

    try:
        resp.raise_for_status()
    except:
        print(f"failed creating connector: {json.dumps(resp.json(), indent=2)}")
        exit(1)
    print("connector created successfully.")
    print("Use kafka-console-consumer and kafka-topics to see data!")

if __name__ == "__main__":
    configure_connector()