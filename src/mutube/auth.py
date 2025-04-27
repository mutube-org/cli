from googleapiclient import discovery
from .config import get_api_key


def initialize_youtube_client():
    api_service_name = "youtube"
    api_version = "v3"

    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "YouTube API key not found. Please set it using 'mutube key YOUR_API_KEY'"
        )

    youtube = discovery.build(api_service_name, api_version, developerKey=api_key)

    return youtube
