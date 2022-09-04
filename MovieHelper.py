import json
import datetime

from requests_html import HTMLSession

now_showing = 'now_showing'
coming_soon = 'coming_soon'


class Movie:
    def __init__(self, movie_name, url, has_ticket, movie_rating, movie_id, movie_length=None, genre=None, language=None, showing=False, is3d=None, sold_out=None, reservable=None):
        self.movie_name = movie_name
        self.youtube_url = url
        self.has_ticket = has_ticket
        self.movie_id = movie_id
        self.movie_length = movie_length
        self.movie_rating = movie_rating
        self.genre = genre
        #self.release_date = release_date
        self.language = language
        self.book_url = f"https://www.qfxcinemas.com/show?eventId={movie_id}"
        self.description = f"3D - {is3d}, Reservable - {reservable}, Sold Out - {sold_out}" if showing else f"{movie_length} mins | {genre} | Tickets Available!!!" if self.has_ticket else f"{movie_length} mins | {genre} |  Tickets Available Soon"


def get_coming_soon_movies():
    try:
        s = HTMLSession()
        r = s.get('https://api.qfxcinemas.com/api/public/ComingSoon')

        response = json.loads(r.html.html)
        movies = [Movie(movie_name=movie['name'], has_ticket=movie['hasBuyTicket'],
                        url=movie['mobileTrailerURL'],
                        movie_id=movie['id'],
                        language=movie['comments'],
                        genre=movie['genre'],
                       # release_date=datetime.datetime.strptime(movie['dtLocalRelease'], '%Y-%m-%dT%H:%M:%S'),
                        movie_length=movie['lengthInMinutes'],
                        movie_rating=movie['eventRating'],
                        )
                  for movie in response['data']]
        return movies

    except Exception as e:
        print(e)


def get_now_showing_movies():
    try:
        s = HTMLSession()
        r = s.get('https://api.qfxcinemas.com/api/public/NowShowing')

        response = json.loads(r.html.html)
        movies = [Movie(movie_name=movie['name'], has_ticket=True,
                        url=movie['mediaLink'],
                        movie_id=movie['eventID'],
                        showing=True,
                        is3d=movie['is3DMovie'],
                        sold_out=movie['soldOut'],
                        reservable=movie['isReservable'],
                        movie_rating=movie['eventRating'],
                        )
                  for movie in response['data']]
        return movies

    except Exception as e:
        print(e)


def get_movies(provider):
    if provider == coming_soon:
        return get_coming_soon_movies()
    elif provider == now_showing:
        return get_now_showing_movies()
    else:
        return []
