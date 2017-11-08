import webbrowser

class Movie():
    """Encapsulate some movies information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title # the movie's title
        self.storyline = movie_storyline# the movies's storyline
        self.poster_image_url = poster_image# the movies's  poster image url
        self.trailer_youtube_url = trailer_youtube# the movies's trailer url

    def show_trailer(self):
        # open browser and play the movie's trailer
        webbrowser.open(self.trailer_youtube_url)