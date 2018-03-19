import movie
import predict
stored_movie_data = []
stored_movie_ratings = []

def rate(m,rating):
	global stored_movie_data
	global stored_movie_ratings
	movie_data = movie.translateToML(movie.getMLFromName(m))
	stored_movie_data.append(movie_data)
	stored_movie_ratings.append(rating)
	pass

while (True):
	stored_movie_data
	stored_movie_ratings
	choice = raw_input("Rate or Predict?(r/p)")
	if "r" in choice:
		movie_name = raw_input("Movie Name: ")
		related_movies = [movie_name] + movie.getRelatedFromName(movie_name)
		rating = raw_input("Love it(l)? Don't Mind it(m)? Hate it(h)?")
		if "l" in rating:
			for m in related_movies:
				try:
					print m
					rate(m,"Love it")
				except:
					print " Error at: "+m
		elif "m" in rating:
			for m in related_movies:
				try:
					print m
					rate(m,"Not Mind it")
				except:
					print " Error at: "+m
		else:
			for m in related_movies:
				try:
					print m
					rate(m,"Hate it")
				except:
					print " Error at: "+m

		print "Rating Stored!"
		#rate
	else:
		movie_name = raw_input("Movie Name: ")
		movie_data = movie.translateToML(movie.getMLFromName(movie_name))
		prediction = predict.predictMovieKNN(movie_data,stored_movie_data,stored_movie_ratings)
		print "You will "+str(prediction[0])
		#predict
