import movie  #import movie.py which contains the Movie class
import fresh_tomatoes  #the python file that turn these codes to a website

# the followings are objects/instances of class Movie
inside_out = movie.Movie("Inside Out",
	                     "https://2.bp.blogspot.com/-x6g88hXjLlU/VYQrLkr-g2I/AAAAAAABRdY/KSxMrT3XS90/s1600/Stacey-Aoyama-Eric-Tan-Inside-Out-Movie-Poster-Disney-2015.jpg",
	                     "https://www.youtube.com/watch?v=_MC3XuMvsDI")

doctor_strange = movie.Movie("Doctor Strange",
                             "http://cdn3-www.comingsoon.net/assets/uploads/gallery/doctor-strange-1403135280/12984033_10154013195382488_6227575399854132650_o.jpg",
                             "https://www.youtube.com/watch?v=kNdM7b1Lm04")

up = movie.Movie("UP",
	             "http://vignette3.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",
	             "https://www.youtube.com/watch?v=pkqzFUhGPJg")

life_of_pi = movie.Movie("Life of Pi",
	                     "http://www.impawards.com/2012/posters/life_of_pi_ver4.jpg",
	                     "https://www.youtube.com/watch?v=mZEZ35Fhvuc")

curious = movie.Movie("The Curious Case of Benjamin Button",
                      "https://yourmomrocks.files.wordpress.com/2013/04/the-curious-case-of-benjamin-button-for-your-consideration.png",
                      "https://www.youtube.com/watch?v=VqeqaweXBV0")

legends = movie.Movie("Legends of the Fall",
                      "http://static.rogerebert.com/uploads/movie/movie_poster/legends-of-the-fall-1995/large_uh0sJcx3SLtclJSuKAXl6Tt6AV0.jpg",
                      "https://www.youtube.com/watch?v=ocAeBZdSDWg")

# put all the objects into a list
movie_list = [inside_out, doctor_strange, up, life_of_pi, curious, legends]

# run fresh_tomatoes
fresh_tomatoes.open_movies_page(movie_list)
