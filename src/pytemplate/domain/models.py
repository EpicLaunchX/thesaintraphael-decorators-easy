from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    customer_age: int

    def __post_init__(self):
        if self.customer_age < 0:
            raise ValueError("customer_age cannot be negative")
