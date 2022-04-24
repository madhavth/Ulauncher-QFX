now_showing = 'now_showing'
coming_soon = 'coming_soon'


class Movie:
    def __init__(self, movie_name, url, has_ticket):
        self.movie_name = movie_name
        self.url = url
        self.has_ticket = has_ticket
        self.description = self.get_description()

    def get_description(self):
        return "Tickets available" if self.has_ticket else "No tickets available"


def get_coming_soon_movies():
    return [Movie(movie_name='Testing', has_ticket=False,
                  url='https://www.google.com'
                  )]


def get_now_showing_movies():
    return [Movie(movie_name='Testing', has_ticket=True,
                  url='https://www.google.com'
                  )]


def get_movies(provider):
    if provider == coming_soon:
        return get_coming_soon_movies()
    elif provider == now_showing:
        return get_now_showing_movies()
    else:
        return []
