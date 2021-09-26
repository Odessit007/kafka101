from faker import Faker


class User:
    def __init__(self, email: str, first_name: str, last_name: str,
                 age: int, address: str, gender: str, job:str, has_childre_under_16: bool):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender
        self.job = job
        self.has_children_under_16 = has_childre_under_16

    def to_json(self) -> dict:
        return self.__dict__

    @classmethod
    def generate_entity(cls):
        fake = Faker()
        gender = fake.random_element(elements=('F', 'M'))
        age = fake.pyint(min_value=12, max_value=78, step=1)
        return User(
            first_name=fake.first_name_female() if gender == 'F' else fake.first_name_male(),
            last_name=fake.last_name_female() if gender == 'F' else fake.last_name_male(),
            email=fake.email(),
            address=fake.address(),
            age=age,
            job=fake.job(),
            gender=gender,
            has_childre_under_16=fake.pybool() if age in (19, 60) else False
        )
