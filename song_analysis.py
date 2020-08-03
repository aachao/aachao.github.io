import requests
import json
import datetime
import dateutil.parser
import time

token = 'BQDVr_6EsjNWoqRWqtw2kvNnxx5mcK4QtVGv39UZVTfxlv16Tv0l1fD0R25r4BtQzKNXujD8o4tCGqCxrds9wgM0FecUSnZzmPJGesIW61CgdW03KOPMjWqAWSjbwj8s4EhWdWYcdvyEsKwzSzW6eRQoJG_p-w'

headers = {
  'Authorization': 'Bearer {0}'.format(token),
  'Content-Type': 'application/json'
}

songs = []
next_url = 'https://api.spotify.com/v1/me/tracks?limit=50'

while next_url:
	resp = requests.get(next_url, headers=headers).json()
	songs.extend(resp['items'])
	print(len(songs))
	next_url = resp['next']

songs_by_month = dict()

for song in songs:
	ts = dateutil.parser.isoparse(song["added_at"])
	month = str(ts.month) + '-' + str(ts.year)
	if month in songs_by_month:
		songs_by_month[month].append(song)
	else:
		songs_by_month[month] = [song]


genre_count_for_period = dict()
genre_to_artists = dict()
for k in ['1-2019', '2-2019', '12-2018']:
	genre_count = dict()
	songs = songs_by_month[k]
	for song in songs:
		print(song['track']['name'])

		# Get genres for track
		genres = set()
		for artist in song['track']['artists']:
			token = 'BQBsq8PiIt_tJn9zmrd2buFTbq57F9Ff6xr1JebAAzm5TrRR3gP22ssEF9P1ub_YoKUa05CDFThB_A7WLEyrI5iCYuCsGlftqwEHHiA3_3cP4GF8eAmtf-xq5QH9Ia-cJo22DFCOD3PYSBhjjd5C6Uh9CA9Dvw'
			headers = {
			  'Authorization': 'Bearer {0}'.format(token),
			  'Content-Type': 'application/json'
			}

			resp = requests.get('https://api.spotify.com/v1/artists/' + artist['id'], headers=headers).json()
			if 'genres' not in resp:
				time.sleep(10)
				resp = requests.get('https://api.spotify.com/v1/artists/' + artist['id'], headers=headers).json()
			for genre in resp['genres']:
				genres.add(genre)
				if genre not in genre_to_artists:
					genre_to_artists[genre] = set()
				genre_to_artists[genre].add(artist['name'])

        # Update genre counters
		for genre in genres:
			if genre in genre_count_for_period:
				genre_count_for_period[genre] += 1
			else:
				genre_count_for_period[genre] = 1

sorted_genre_count = sorted(genre_count_for_period.items(), key=lambda x: x[1], reverse=True)
print(sorted_genre_count)
import pdb
pdb.set_trace()
# print(genre_to_artists['post-teen pop'])
# print(genre_to_artists)









# mysong = songs[0]
# ts = dateutil.parser.isoparse(mysong["added_at"])

# print(ts.month)
