from googleapiclient.discovery import build
from dotenv import load_dotenv 
import os
import json

# Maximum results per page in response
MAX_RESULTS = '50'
CHANNEL_ID = 'UC5FNZuDRFVPArJ-4EI3hLUQ'

# Returns a response of playlistItems given a playlistId and pageToken
def get_playlistitems_response(id, page_token):
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=id,
        maxResults=MAX_RESULTS,
        pageToken=page_token,
    )

    return request.execute()

# Prints the titles of a playlistItems response
def print_playlistitems_titles_from_response(response):
    playlistitems_list = response['items']

    for playlistitem in playlistitems_list:
        print(playlistitem['snippet']['title'])

# Get a list of playlistItems by playlist id
def get_playlistitems_titles_by_id(id):
    # First page doesn't need token
    page_token = ''

    # Get and print the response
    response = get_playlistitems_response(id, page_token)
    print_playlistitems_titles_from_response(response)

    # Check if the response includes a token for additional results pages
    while 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
        response = get_playlistitems_response(id, next_page_token)
        print_playlistitems_titles_from_response(response)
    
# Load from .env
load_dotenv()

# Create "service object"
youtube = build('youtube', 'v3', developerKey=os.getenv("API_KEY"))

# Form the request with a given channelId
request = youtube.playlists().list(
    part='snippet',
    channelId=CHANNEL_ID,
)

response = request.execute()
playlist_list = response['items']

# Iterate through the playlist returned
for playlist in playlist_list:
    # Title of playlist
    print(playlist['snippet']['title'])
    # ID
    print(playlist['id'])
    get_playlistitems_titles_by_id(playlist['id'])
    print()

# Close the connection
youtube.close()

