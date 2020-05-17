import json
import requests

# confluent local load jdbc_source_mysql_posts -- -d /tmp/jdbc_source_mysql_posts.json
# curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{\n        "name": "codegen-file",\n        "config": {\n  "name": "codegen-file",\n  "connector.class": "org.apache.kafka.connect.file.FileStreamSourceConnector",\n  "tasks.max": "1",\n  "key.converter": "org.apache.kafka.connect.json.JsonConverter",\n  "value.converter": "org.apache.kafka.connect.json.JsonConverter",\n  "file": "/Users/sampatbudankayala/Documents/sampat/Data/mysql_data/posts.csv",\n  "topic": "com.simpplr-posts",\n  "batch.size": "20"\n}\n        }'
# curl -s "http://localhost:8083/connectors/codegen-file/status"| jq '.'
# curl -s "http://localhost:8083/connectors"

KAFKA_CONNECT_URL = "http://ec2-35-175-221-118.compute-1.amazonaws.com:28083/connectors"
CONNECTOR_NAME = "jdbc_source_mysql_debezium_test2"


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
                "name": "jdbc_source_mysql_debezium_test2",  # TODO
                    "config": {
                        "connector.class": "io.debezium.connector.mysql.MySqlConnector",
                        "tasks.max": "1",
                        "database.hostname": "simpplr-aurora-mvp.cluster-c8rc5b77uwdw.us-east-1.rds.amazonaws.com",
                        "database.port": "3306",
                        "database.user": "root",
                        "database.password": "sIhz4XjabyiTkZIwmT9g",
                        "database.server.id": "43013504",
                        "database.server.name": "rds_aur_test2",
                        "database.whitelist": "test2",
                        "database.history.kafka.bootstrap.servers": "b-2.simpplr-msk-cdc.3wachc.c6.kafka.us-east-1.amazonaws.com:9092,b-3.simpplr-msk-cdc.3wachc.c6.kafka.us-east-1.amazonaws.com:9092,b-1.simpplr-msk-cdc.3wachc.c6.kafka.us-east-1.amazonaws.com:9092",
                        "database.history.kafka.topic": "schema-changes.test2"
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