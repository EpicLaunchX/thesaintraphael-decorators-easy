from functools import wraps
from typing import Callable

from pytemplate.domain.models import Movie


def age_limit_6plus(func: Callable[[Movie], str]) -> Callable[[Movie], str]:

    @wraps(func)
    def wrapper(movie: Movie) -> str:
        if movie.customer_age >= 6:
            return func(movie)
        return f"Sorry, you are not old enough to watch {movie.name}!"

    return wrapper
