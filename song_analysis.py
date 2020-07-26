import requests
import json
import datetime
import dateutil.parser

token = 'BQBzsIarGNN3cEdSqf4YuexCCNSitYCUukr_9pIduN4x-ir7srhrxA4CDeR1_RSom8tWwX3eAuyVlcqAUP3CDgtXBXCWSKfYAckCA94a3xhvpZHefed1vu0pgQkuCU5DMGu_ceMvnce0FywAMYadfcubtz_lOA'

headers = {
  'Authorization': 'Bearer {0}'.format(token),
  'Content-Type': 'application/json'
}

songs = []
next_url = 'https://api.spotify.com/v1/me/tracks?limit=50'

while next_url:
	resp = requests.get(next_url, headers=headers).json()
	songs.extend(resp["items"])
	print(len(songs))
	next_url = resp["next"]

songs_by_month = dict()

for song in songs:
	ts = dateutil.parser.isoparse(song["added_at"])
	month = str(ts.month) + '-' + str(ts.year)
	if month in songs_by_month:
		songs_by_month[month].append(song)
	else:
		songs_by_month[month] = [song]

# print(len(songs_by_month))
# for k in songs_by_month:
# 	print(len(songs_by_month[k]))

popular_song_by_month = dict()

for k in songs_by_month:
	songs = songs_by_month[k]
	cur_popularity = 0
	for song in songs:
		if song['track']['popularity'] > cur_popularity:
			popular_song_by_month[k] = song
			cur_popularity = song['track']['popularity']

for k in popular_song_by_month:
	print(popular_song_by_month[k]['track']['name'])



# mysong = songs[0]
# ts = dateutil.parser.isoparse(mysong["added_at"])

# print(ts.month)
