==================================================================================================================

This program fetches Movie information based on the Movie title and can be run with arguments or interactively. 
API - http://www.omdbapi.com 

Args:
    -m, --movie : Enter your Movie Title
	-h, --help : Help Menu 
	
==================================================================================================================

RUN: From Docker Container

Option#1: 
docker run -it sdnguru22/derrcart_movie_app:v1 -m <Movie Title>

Option#2:
docker run -it sdnguru22/derrcart_movie_app:v1
Please Enter you Movie Title: <Movie Title>

==================================================================================================================

RUN: From Bash 

Option#1: 
python get_movie.py -m <Movie Title>

Option#2:
python get_movie.py
Please Enter you Movie Title: <Movie Title>
 
==================================================================================================================
