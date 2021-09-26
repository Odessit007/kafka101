from random import Random
from time import sleep

from entities.product import Product
from entities.user import User


class BaseGenerator:
    @classmethod
    def generate(cls, data_class, n_batches, batch_size_min, batch_size_max):
        for i in range(n_batches):
            batch_size = Random().randint(batch_size_min, batch_size_max)
            batch = [data_class.generate_entity() for _ in range(batch_size)]
            yield batch
            sleep(5)


class ProductGenerator(BaseGenerator):
    @classmethod
    def generate_records(cls, n_batches=10, batch_size_min=50, batch_size_max=100):
        yield from super().generate(Product, n_batches, batch_size_min, batch_size_max)


class UserGenerator(BaseGenerator):
    @classmethod
    def generate_records(cls, n_batches=10, batch_size_min=50, batch_size_max=100):
        yield from super().generate(User, n_batches, batch_size_min, batch_size_max)


def get_generator(entity):
    if entity == 'user':
        return UserGenerator
    elif entity == 'product':
        return ProductGenerator
