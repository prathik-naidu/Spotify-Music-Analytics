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

