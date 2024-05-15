from googleapiclient.discovery import build
from dotenv import load_dotenv 
import os
import json

# Load from .env
load_dotenv()

# Create "service object"
youtube = build('youtube', 'v3', developerKey=os.getenv("API_KEY"))

# Form the request
request = youtube.playlists().list(
    part='snippet',
    channelId='UC5FNZuDRFVPArJ-4EI3hLUQ',
)

response = request.execute()

print(json.dumps(response, sort_keys=True, indent=4))

# Close the connection
youtube.close()