from googleapiclient.discovery import build
import os
import json


youtube = build('youtube', 'v3', developerKey=os.environ["API_KEY"])

# request = youtube.channels().list(
#     part='statistics',
#     forHandle='pepsivstim'
# )

# response = request.execute()

# print(json.dumps(response, sort_keys=True, indent=4))

request = youtube.playlists().list(
    part='snippet',
    channelId='UC5FNZuDRFVPArJ-4EI3hLUQ',
)

response = request.execute()

#print(response)
#print(json.dumps(response, sort_keys=True, indent=4))