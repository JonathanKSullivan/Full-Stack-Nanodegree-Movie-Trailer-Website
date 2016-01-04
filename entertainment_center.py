import media
import fresh_tomatoes

starwars7 = media.Movie("Star Wars: Episode VII",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://youtu.be/sGbxmsDFVnE", "A continuation of the saga created by George Lucas and set thirty years after Star Wars: Episode VI - Return of the Jedi (1983).")
movies = [starwars7]
fresh_tomatoes.open_movies_page(movies)
