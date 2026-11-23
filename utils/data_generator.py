from faker import Faker

fake = Faker()


def generate_first_name() -> str:
    return fake.first_name()


def generate_middle_name() -> str:
    return fake.first_name()


def generate_last_name() -> str:
    return fake.last_name()


def generate_employee_id() -> str:
    return fake.numerify(text="########")
