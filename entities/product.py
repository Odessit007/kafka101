from faker import Faker


class Product:
    cat2range = {
        'toys': (1, 100),
        'books': (1, 1000),
        'computers and accessories': (10, 5000),
        'instruments': (1, 1000),
        'drugs': (1, 1000),
        'clothes': (10, 500)
    }
    categories = list(cat2range.keys())

    def __init__(self, barcode: str, category: str, name: str, price: float, color: str, producer_country: str):
        self.barcode = barcode
        self.category = category
        self.name = name
        self.price = price
        self.color = color
        self.producer_country = producer_country

    def to_json(self) -> dict:
        return self.__dict__

    @classmethod
    def generate_random_product(cls):
        fake = Faker()
        category = fake.random_element(elements=cls.categories)
        min_value, max_value = cls.cat2range[category]
        return Product(
            barcode=fake.ean(),
            category=category,
            name=fake.pystr(min_chars=5, max_chars=15),
            price=fake.pyfloat(right_digits=2, min_value=min_value, max_value=max_value),
            color=fake.color_name(),
            producer_country=fake.country()
        )
