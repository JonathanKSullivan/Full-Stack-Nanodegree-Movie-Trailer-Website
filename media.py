import webbrowser
class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube, movie_storyline):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.youtube_url)
        
