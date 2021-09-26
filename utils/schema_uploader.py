from confluent_kafka import avro


class SchemaUploader:
    @staticmethod
    def load_avro_schema_from_file(schema_file):
        key_schema = avro.loads('{"type": "string"}')
        value_schema = avro.load(f'./schema/{schema_file}')
        return key_schema, value_schema
