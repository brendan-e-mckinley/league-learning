import requests
import json

# Your Spotify API credentials
CLIENT_ID = '30b6bb6dd13148a3a931512843045985'
CLIENT_SECRET = '8fab50e3f26041fba4f747f51d7e779d'

# Authentication URL for the API
auth_url = 'https://accounts.spotify.com/api/token'

# Get the access token
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})
auth_data = auth_response.json()
access_token = auth_data['access_token']
playlist_ids = [ '5ar11OclJqsYf6BN9HpnMJ',
                 '60kiCLFDdqiy0LPNTMUnI8', 
                 '2t3OXAiOu6ecCC0NM3K1i7',
                 '3OwlEI2HicQfnYNWQtgx0i',
                 '72g2u1IrgnGdCAugmR7iAG',
                 '1A1rgbJkZTSNWgtKMAFlmM',
                 '4ImUFNgR1FM0i8EBlRVmfP',
                 '6uEhpTwCk8e4sku8pymkPV',
                 '41Ez0yZTJUhY95OC65HYuu',
                 '1XRSsP9CjgOrMCN6OJ6gpf' ]
    
file_string = ""
file_string_with_names = ""

for playlist_id in playlist_ids:
    # Get the tracks from the playlist
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    playlist_response = requests.get(playlist_url, headers=headers)
    playlist_data = playlist_response.json()

    print(playlist_data)

    # index
    counter = 1

    # Extract release date for each track
    for track in playlist_data['items']:
        song_name = track['track']['name']
        release_date = track['track']['album']['release_date']
        if "-" in release_date:
            release_date = release_date[:4]
        file_string += str(counter) + ' ' + release_date + '\n'
        file_string_with_names += str(counter) + ' ' + release_date + ' ' + song_name + '\n'
        counter += 1

with open('input_data.txt', 'w') as output:
    output.write(file_string)

with open('input_data_with_names.txt', 'w') as output:
    output.write(file_string_with_names)