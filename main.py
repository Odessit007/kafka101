from argparse import ArgumentParser
import logging

from generator.generators import get_generator
from producers.producers import get_producer


logging.basicConfig(level=logging.INFO)


def parse_args():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--entity', required=True, help='Entity (user or product)', choices=('user', 'product'))
    arg_parser.add_argument('--topic', required=True, help='Topic name')
    arg_parser.add_argument('--bs', required=False, default='localhost:9092', help='Bootstrap server URL')
    arg_parser.add_argument('--sr', required=False, default='http://localhost:8081', help='Schema registry URL')
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    entity = args.entity
    schema_file = 'product.avsc' if entity == 'product' else 'user.avsc'
    producer = get_producer(entity, args.topic, schema_file, args.bs, args.sr)
    generator = get_generator(entity)
    for records_batch in generator.generate_records():
        producer.send_records(records_batch)
