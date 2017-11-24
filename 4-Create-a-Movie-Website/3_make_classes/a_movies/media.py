# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    '''This class provides a way to store movie related information'''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        # initialize instance of class Movie
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        # open the youtube trailer in the default web browser
        webbrowser.open(self.trailer_youtube_url)
        
