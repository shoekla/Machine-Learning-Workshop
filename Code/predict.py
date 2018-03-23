"""
This file will be edited and used during
the workshop to predict movie ratings using
Scikit-Learn and Numpy
"""

"""
This file will be edited and used during
the workshop to predict movie ratings using
Scikit-Learn and Numpy
"""
#def predictMovieKNN(new_movie_info,features,labels):
#Dummy Features: [140,1], [130, 1], [150,0], [170, 0]
#Dummy Labels: "Apple", "Apple", "Orange","Orange"

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def predictMovieKNN(new_movie_info,features,labels):
	neigh = KNeighborsClassifier(n_neighbors=1)
	neigh.fit(features,labels)
	return neigh.predict(np.array(new_movie_info).reshape(1,-1))







