# config for website_checker
WEBSITE = 'https://aiven.io'
WEBSITE_TITLE = 'Aiven Database as a Service | Your data cloud'

# config for pg_client
POSTGRES_HOST = 'pg-275744ab-ece-8ede.aivencloud.com'
POSTGRES_DB = 'metrics'
POSTGRES_USER = 'avnadmin'
POSTGRES_PWD = 'u69rl0w70ou16ipg'
POSTGRES_PORT = '12536'


METRICS_TABLE = 'aiven_metrics'


#Kafka details
KAFKA_HOST = 'sam-kafka-ece-8ede.aivencloud.com:12538'
CA_FILE = "ca.pem"
CERT_FILE = "service.cert"
KEY_FILE = "service.key"
TOPIC = "metrics"