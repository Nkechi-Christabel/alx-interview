#!/usr/bin/python3
"""
A script that prints all characters of a Star Wars movie.
"""

import sys
import requests


def fetch_movie_characters(movie_id):
    """
    Fetch and print all characters of a Star Wars movie based on the given Movie ID.

    Parameters:
    - movie_id (str): The ID of the Star Wars movie.

    Returns:
    - None
    """
    try:
        # Fetch movie details using the provided Movie ID
        url = f"https://swapi.dev/api/films/{movie_id}/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        movie_data = response.json()
        characters = movie_data.get('characters', [])

        # Fetch and print each character's name
        for character_url in characters:
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()
            print(character_data['name'])
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    movie_id = sys.argv[1]

    if not movie_id.isdigit():
        print("Movie ID must be a number")
        sys.exit(1)
    
    fetch_movie_characters(movie_id)
