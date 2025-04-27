import requests


def get_video_snippet(youtube, video_id):
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    return response


def get_video_statistics(youtube, video_id):
    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()
    return response


def get_channel_id_from_video_id(youtube, video_id):
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    return response["items"][0]["snippet"]["channelId"]


def is_short(video_id):
    short_url = f"https://www.youtube.com/shorts/{video_id}"
    try:
        response = requests.head(short_url, allow_redirects=False)
        if response.status_code == 200:
            return True

        if 300 <= response.status_code < 400:
            return False

        return False

    except Exception:
        return False


def find_nearby_videos(youtube, video_id):
    channel_id = get_channel_id_from_video_id(youtube, video_id)
    video_snippet = get_video_snippet(youtube, video_id)
    video_published_at = video_snippet["items"][0]["snippet"]["publishedAt"]

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        order="date",
        maxResults=50,
        publishedBefore=video_published_at,
    )
    response = request.execute()
    num_videos = 0
    videos = []
    for video in response["items"]:
        if not is_short(video["id"]["videoId"]):
            num_videos += 1
            videos.append(video)
            if num_videos >= 10:
                break

    for video in videos:
        video_id = video["id"]["videoId"]
        stats = get_video_statistics(youtube, video_id)
        if "items" in stats and len(stats["items"]) > 0:
            video["statistics"] = stats["items"][0]["statistics"]
        else:
            video["statistics"] = {"viewCount": "0"}

    return videos
