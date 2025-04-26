from auth import initialize_youtube_client
import os
from dotenv import load_dotenv
from rich import print

def get_channel_info(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet",
        id=channel_id
    )
    response = request.execute()
    return response

def get_channel_uploads_playlist(youtube, channel_id):
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

if __name__ == "__main__":
    youtube = initialize_youtube_client()
    load_dotenv()
    lukej_channel_id = os.getenv("LUKEJ_CHANNEL_ID")
    print(get_channel_uploads_playlist(youtube, lukej_channel_id))
