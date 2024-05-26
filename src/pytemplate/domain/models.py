from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    customer_age: int

    def __post_init__(self):
        if not isinstance(self.customer_age, int):
            raise TypeError("customer_age must be an integer")
        if self.customer_age < 0:
            raise ValueError("customer_age cannot be negative")


def movie_factory(name: str, customer_age: int) -> Movie:
    return Movie(name=name, customer_age=customer_age)
