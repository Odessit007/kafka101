import logging

from confluent_kafka.avro import AvroProducer

from utils.schema_uploader import SchemaUploader


class BaseProducer:
    def __init__(self, topic, schema_file, bootstrap_server_url, schema_registry_url):
        self.topic = topic
        key_schema, value_schema = SchemaUploader.load_avro_schema_from_file(schema_file)
        producer_config = {
            'bootstrap.servers': bootstrap_server_url,
            'schema.registry.url': schema_registry_url
        }
        self.producer = AvroProducer(
            config=producer_config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )

    def send_record(self, key: str, value: dict):
        record_repr = f'record with key={key}, value={value} to topic {self.topic}'
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            logging.error(f'Exception happened while producing {record_repr}: {e}')
        else:
            logging.info(f'Successfully produced {record_repr}')

    def send_records(self, records):
        for record in records:
            self.send_record(key=self.key_extractor(record), value=self.value_extracotr(record))
        self.producer.flush()

    def key_extractor(self, record):
        raise NotImplementedError

    def value_extracotr(self, record):
        raise NotImplementedError


class ProductProducer(BaseProducer):
    def key_extractor(self, product):
        raise product.barcode

    def value_extracotr(self, product):
        raise product.to_json()


class UserProducer(BaseProducer):
    def key_extractor(self, user):
        raise user.email

    def value_extracotr(self, user):
        raise user.to_json()


def get_producer(entity, topic, schema_file, bootstrap_server_url, schema_registry_url):
    if entity == 'product':
        return ProductProducer(topic, schema_file, bootstrap_server_url, schema_registry_url)
    elif entity == 'user':
        return UserProducer(topic, schema_file, bootstrap_server_url, schema_registry_url)
