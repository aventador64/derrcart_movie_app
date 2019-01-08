"""
This program fetches Movie information based on the Movie title and can be run with arguments or interactively. 
API - http://www.omdbapi.com 
"""
import re
import json
import argparse
import requests

__author__ = 'derrcart@cisco.com'

def get_movie(movie_title):
    """
    :param movie_title:
    """
    
    url = 'http://www.omdbapi.com/?t=' + movie_title + '&apikey=ab0cd81d'
    r = requests.post(url)
    my_response = r.json()

    bold_s = "\033[1m"
    bold_e = "\033[0;0m"
    print '======================================================================'
    print(bold_s + my_response['Title'] + bold_e + ' Movie Details' + '\n')
    print '======================================================================'  

    print(bold_s + 'Title: ' + bold_e + my_response['Title'] + '\n')

    print(bold_s + 'Release Date: ' + bold_e  + my_response['Released'] + '\n')

    print(bold_s + 'Movie Run Time: ' + bold_e  + my_response['Runtime'] + '\n')

    print(bold_s + 'Genre: ' + bold_e  + my_response['Genre'] + '\n')

    print(bold_s + 'Cast: ' + bold_e  + my_response['Actors'] + '\n')

    print(bold_s + 'Story: ' + bold_e  + my_response['Plot'] + '\n')

    print(bold_s + 'Rotten Tomatoes: ' + bold_e  + my_response['Ratings'][1]['Value'] + ' Fresh!')
    print '======================================================================'

def main():
    """
    Set args and get user input movie title
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--movie', help="What is your Movie Title")
    parser.add_argument('arg', nargs='*') 
    parsed = parser.parse_args()
    
    movie_title = parsed.movie

    if parsed.movie is None:
        movie_title = raw_input('Please Enter you Movie Title: ')

    get_movie(movie_title)
    
if __name__ == "__main__":
    main()
