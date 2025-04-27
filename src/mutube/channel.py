from .auth import initialize_youtube_client


def get_channel_info(youtube, channel_id):
    request = youtube.channels().list(part="snippet", id=channel_id)
    response = request.execute()
    return response


def get_channel_uploads_playlist(youtube, channel_id):
    request = youtube.channels().list(part="contentDetails", id=channel_id)
    response = request.execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
