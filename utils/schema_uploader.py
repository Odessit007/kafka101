from confluent_kafka import avro


class SchemaUploader:
    @staticmethod
    def load_avro_schema_from_file(schema_file):
        key_schema = avro.loads('{"type": "string"}')
        value_schema = avro.load(f'./schemas/{schema_file}')
        return key_schema, value_schema


if __name__ == '__main__':
    print(SchemaUploader.load_avro_schema_from_file('product.avsc'))
