import random
import requests
import string
import urllib

#Initializing the class
class SpotifyClient(object):
	def __init__(self, api_token):
		self.api_token = api_token
	#Generationg random tracks from the spotify api
	def get_random_tracks(self):
		wildcard = f'%{random.choice(string.ascii_lowercase)}%'
		query = urllib.parse.quote(wildcard)
		offset = random.randint(0, 2000)
		url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
		response = requests.get(
			url,
			headers={
				"Content-Type": "application/json",
				"Authorization": f"Bearer {self.api_token}"
			}
		)
		response_json = response.json()

		tracks = [
			track for track in response_json['tracks']['items']
		]

		print(f'Found {len(tracks)} tracks to add to your library') #Giving number of tracks (20 as per api non-premium account limit)

		return tracks

	#Adding tracks to your library
	def add_tracks_to_library(self, track_ids):
		url = "https://api.spotify.com/v1/me/tracks"
		response = requests.put(
			url,
			json={
				"ids": track_ids
			},
			headers={
				"Content-Type": "application/json",
				"Authorization": f"Bearer {self.api_token}"
			}
		)
		
		return response.ok