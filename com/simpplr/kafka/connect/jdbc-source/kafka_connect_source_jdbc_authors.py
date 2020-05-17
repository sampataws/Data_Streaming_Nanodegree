import json
import requests

# confluent local load jdbc_source_mysql_posts -- -d /tmp/jdbc_source_mysql_posts.json
# curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{\n        "name": "codegen-file",\n        "config": {\n  "name": "codegen-file",\n  "connector.class": "org.apache.kafka.connect.file.FileStreamSourceConnector",\n  "tasks.max": "1",\n  "key.converter": "org.apache.kafka.connect.json.JsonConverter",\n  "value.converter": "org.apache.kafka.connect.json.JsonConverter",\n  "file": "/Users/sampatbudankayala/Documents/sampat/Data/mysql_data/posts.csv",\n  "topic": "com.simpplr-posts",\n  "batch.size": "20"\n}\n        }'
# curl -s "http://localhost:8083/connectors/codegen-file/status"| jq '.'
# url -s "http://localhost:8083/connectors"

KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "jdbc_source_mysql_authors"


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
                "name": "jdbc_source_mysql_authors-jdbc",  # TODO
                    "config": {
                        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",  # TODO
                        "topic.prefix": "connect-mysql-",  # TODO
                        "mode": "incrementing",  # TODO
                        "incrementing.column.name": "id",  # TODO
                        "table.whitelist": "authors",  # TODO
                        "tasks.max": 1,
                        "connection.url": "jdbc:mysql://localhost:3306/simpplr?user=root&password=password",
                        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                        "key.converter.schemas.enable": "false",
                        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                        "value.converter.schemas.enable": "false"
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