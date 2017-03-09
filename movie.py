#this file defines a class with functions used in media_center.py
import webbrowser

class Movie():
    def __init__(self, movie_title,poster_image,movie_trailer):  #this gives title,image and movie trailer
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):  #this defines a function to open the trailer
        webbrowser.open(self.movie_trailer)
