# A Simple Machine Learning Workshop 
## Building a Movie Prediction Model using Scikit-Learn

Organizers: Abir Shukla, Pranav Vasudha, Zach Rich, Abid Kaisani and of course Purdue Hackers.


[![N|Solid](https://scontent-ort2-1.xx.fbcdn.net/v/t31.0-8/22218441_1820975817931104_3605371181666717728_o.jpg?oh=117197081841929c2d86a1d02198df9a&oe=5B1E5ADF)](https://purduehackers.com/)

Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. While some might find Machine Learning as a daunting subject, it can be utilized with high level libraries sub as scikit-learn.


# Scikit-Learn Introduction
http://scikit-learn.org/stable/
  - Simple and efficient tools for data mining and data analysis
  - Accessible to everybody, and reusable in various contexts
  - Open source, commercially usable - BSD license
  - Super Easy to learn and use!

### Installation

ML Workshop requires python2.7 to run.
https://www.python.org/download/releases/2.7/

Install the dependencies:
```sh
$ pip install requests
$ pip install beautifulsoup4
$ python -m pip install --user numpy scipy
$ pip install -U scikit-learn
```

## Part 1: Understanding what ML is and what it does
https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal

## Part 2: Supervised vs Unsupervised Learning

Generally we can categorize a machine learning algrothy into one of 2 "types".

Supervised Learning:
  - Give the model inputs and outputs and let the algorithm learning the mapping function
  - Lets algorithm train by predicting, but supervises the learning process by giving algorithm outputs as well.
  - Classification: Predict a category. (Car, Color, Genre)
  - Regression: Predict a quantity. (Money, Weight, Grade)
  - All data is labeled and the algorithms learn to predict the output from the input data.

Unsupervised Learning:
  - Only give the model inputs and let the model learn about the data on its own
  - No correct answers, just exploring the data
  - Clustering: Find similar data in group. (Groups of customer spending behavior) 
  - Association: Discover rules amongst the data. (Usually if X happens, Y will also occur)
  - All data is unlabeled and the algorithms learn to inherent structure from the input data.

For this workshop we will be using KNN which is a supervised learning algorithm.

## Part 3: Generative vs. Discriminative Models

2 types on models commonly used in machine learning are generative and discriminative models.

Generative Models
  - Cares about how data was generated
  - Based on my generation assumption, which category is most likely to generate the signal

Discriminative Models:
  - Does not care how data was generated, simply categorizes. 
  - Just learns the boundaries, and differences between the data 

## Part 4: The K Nearest Neighbors Algorithm

KNN or K nearest neighbors is a simple machine learning algorithm. Training data is represented as nodes on a graph that represents x dimensions (x represents the number of attributes the training data contains, for the example we use a simple 2 dimensional graph but the algorithm is still the same). Whenever a new node is added the algorithm finds the K nearest nodes, and uses the training on what those nodes are to predict/classify what the new node is. K is usually an odd number that will get an accurate depiction of where the node while settling ties that might occur from an even K value.

![Alt Text](https://raw.githubusercontent.com/shoekla/Machine-Learning-Workshop/master/Docs/knn.gif)

As the gif loops notice new nodes (the blue nodes) are inputted and then connect with their 3 nearest neighbors (3 being the value of K in this example). If all values are the same it turns to that value. If not, the node turns to the color that the majority of the nodes are.




## Part 5: Movies

To make a movie prediction model we need to make a movie turn into a dataset.

![Alt Text](https://raw.githubusercontent.com/shoekla/Machine-Learning-Workshop/master/Docs/movie_graph.png)

What basic attributes can we extract that most films possess:

* IMDB Rating
* Metacritic Rating
* *Genres
* Number of Awards
* Length of Movie
* Related Movies?


### Provided Files

movie.py contains various methods that allow you to extract data from movies using IMDB.


| Method Name | Input | Output |
| ------ | ------ |------ |
|getMLFromName(movie_name)| String: name of movie | Array of attributes |
|translateToML(attribute_array)| Array: list of attributes from movie| Array of attributes that is organized in a way that ml can comprehend |
|getRelatedFromName(movie_name)| String: name of movie | Array of related movie names |

client.py contains a barebones form of IO to interact with the ML model.
predict.py is where we will create methods that will use Machine Learning to train and test our model.

## Part 6: Working with Scikit-Learn

Scikit-Learn requires 2 datasets for training and a 3rd for testing for the KNN algorithm and many others.
* Features: the movie attributes that we acquired for various films
* Labels: our corresponding rating towards that film
* Testing Dataset: movie attributes from a movie not in the 'features' list (only needed to test the model not to train it)

### Let's build a simple model using scikit learn

For a Model to perform the best it can it needs:

* A large dataset
* A quality dataset

Importing Libraries
```sh
$ import numpy as np
$ from sklearn.neighbors import KNeighborsClassifier
```
In our prediction python file (predict.py) we need to use Scikit-Learn which needs numpy.

Initializing the Model
```sh
$ neigh = KNeighborsClassifier(n_neighbors=3)
```
Here we create a KNN model where K=3 and save it to the "neigh" variable.

Training the Model:
```sh
$ neigh.fit(features, labels)
```
Now we need to train the model we just created. We are giving the model a list (2d array) of "features", and a corresponding list (1d array) of "labels".

Prediction using the Model:
```sh
$ neigh.predict(new_movie_info)
```
Now that our model is trained on a dataset, we can ask our model to predict our "labels" toward a new dataset.

## Part 7: Connecting the Movie Data to the Model
Now let's connect our web scraping in movie.py and our machine learning in predict.py using client.py which is how we will interact with our newly created model. The client also is responsible for:

* Fetching related movies for the model to gain more datasets.
* Resolving any errors that come up during the web scraping or prediction process
* Storing datasets used for prediction

Below is a picture of client.py in action. Notice how an error occurs with the move titled "Crazy, Stupid, Love." but continues on, and also notice that only 2 movies were manually given the rest are related movies merge quantity and quality data.

![Alt Text](https://raw.githubusercontent.com/shoekla/Machine-Learning-Workshop/master/Docs/client.png)


### References

This workshop used a number of resources:

* [Expert System] - http://www.expertsystem.com/machine-learning-definition/
* [Machine Learning Mastery] - https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/
* [Scikit-Learn] - http://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/index.html
* [Quora] - https://www.quora.com/What-are-the-differences-between-generative-and-discriminative-machine-learning/answer/Abhinav-Litkar?share=ba930329&srid=DOxE
* [IMDB] - http://www.imdb.com/
* [Purdue Hackers] - https://purduehackers.com/




