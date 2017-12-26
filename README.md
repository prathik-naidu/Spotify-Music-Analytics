# Spotify Music Analytics

A tool to analyze your personal music taste and figure out new songs that your friends are listening to

## Getting Started

The instructions below will walk you through necessary packages needed to the run the tool along with examples on how to make use of the tool's features.

Note: Currently working on developing an application so users do not have to run the program on terminal.

### Prerequisites

Necessary packages for running the tool:

* [Spotipy](https://github.com/plamere/spotipy)
* [pandas](https://pandas.pydata.org/)
* [Numpy/Scipy](https://www.scipy.org/scipylib/download.html)
* [sklearn](http://scikit-learn.org/stable/install.html)

In order to run the tool locally, a spotify client authorization must be obtained. This can be done by registering the application locally through the [Spotify Developer](https://beta.developer.spotify.com/dashboard/login) account.

From here you can type in the following commands on terminal:

```
export SPOTIPY_CLIENT_ID='***From Spotify Developer Portal***'
export SPOTIPY_CLIENT_SECRET='***From Spotify Developer Portal***'
export SPOTIPY_REDIRECT_URI='https://example.com/callback'
```

## Technical Details

This is a python program that handles data acquisition, preprocessing, and model developement. Here are the key steps behind this tool (main method in predict.py):

1. Gets user input from the console to determine which playlists the user likes and dislikes. Subsequently gets the corresponding playlist ID's (spotify URI code) for those playlists.
2. For the liked and disliked playlists, gets the songs in those playlists and calculates audio features for those songs (output in a dataframe). The following audio features were used:
    * Energy
    * Liveness
    * Tempo
    * Speechiness
    * Acousticness
    * Instrumentalness
    * Time Signature
    * Danceability
    * Key
    * Loudness
    * Valence
    * Mode
    * Popularity
    * Explicit (yes or no)
3. Preprocess data to combined the liked and disliked audio features data sets and add in a "target" column which corresponds to the label for the dataset
4. Separate dataset into distinct features and labels data frames
5. Split the features and labels data frames into training and test data
6. Train the models (Random Forest, kNN, Multilayer Perceptron, and Logistic Regression)



