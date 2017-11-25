# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes


kingdom_of_heaven = media.Movie(
    "Kingdom of Heaven",
    "A knight to defend Jerusalem",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/KoHposter.jpg",
    "https://www.youtube.com/watch?v=Kfq9U2tWWGo")

gladiator = media.Movie(
    "Gladiator",
    """A man robbed of his name and dignity strives to win them back and gain
    the freedom of his people""",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE")

alien = media.Movie(
    "Alien",
    """A close encounter of the third kind becomes a Jaws-style nightmare when
    an alien invades a spacecraft""",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
    "https://www.youtube.com/watch?v=LjLamj-b0I8")

pacific_rim = media.Movie(
    "Pacific Rim",
    """A ragtag band of humans banding together to fight monstrous creatures
    from the sea""",
    "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",  # noqa
    "https://www.youtube.com/watch?v=5guMumPFBag")

the_day_after_tomorrow = media.Movie(
    "The Day after Tomorrow",
    """A paleoclimatologist must reach his son trapped in a sudden international
    storm""",
    "https://upload.wikimedia.org/wikipedia/en/5/58/The_Day_After_Tomorrow_movie.jpg",  # noqa
    "https://www.youtube.com/watch?v=Ku_IseK3xTc")

deep_impact = media.Movie(
    "Deep Impact",
    """Humans attempt to destroy a comet expected to collide with the Earth and
    cause a mass extinction""",
    "https://upload.wikimedia.org/wikipedia/en/9/93/Deep_Impact_poster.jpg",
    "https://www.youtube.com/watch?v=NTkfk4dCnu8")

movies = [
    kingdom_of_heaven,
    gladiator,
    alien,
    pacific_rim,
    the_day_after_tomorrow,
    deep_impact
]

fresh_tomatoes.open_movies_page(movies)
