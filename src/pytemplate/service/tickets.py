from pytemplate.domain.models import Movie
from pytemplate.utils.decorator import age_limit_6plus, age_limit_13plus


@age_limit_6plus
def buy_ticket_for_children(movie: Movie) -> str:
    return f"You are allowed to watch {movie.name}!"


@age_limit_13plus
def buy_ticket_for_teens(movie: Movie) -> str:
    return f"You are allowed to watch {movie.name}!"
