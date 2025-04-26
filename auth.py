import os
from dotenv import load_dotenv
from googleapiclient import discovery

def initialize_youtube_client():
    load_dotenv()
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    api_service_name = "youtube"
    api_version = "v3"

    youtube = discovery.build(
        api_service_name, api_version, developerKey=os.getenv("YOUTUBE_API_KEY"))
    
    return youtube