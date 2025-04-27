import requests
from rich import print
from video import is_short, Video
from utils import convert_xml_to_json


def get_rss_feed(channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    response = requests.get(url)
    return convert_xml_to_json(response.text)


def extract_videos_from_rss_feed(rss_feed):
    videos = []
    for entry in rss_feed["feed"]["entry"]:
        video_id = entry["yt:videoId"]
        title = entry["title"]
        videos.append(Video(video_id, title))
    return videos


if __name__ == "__main__":
    rss_feed = get_rss_feed("UCYzV77unbAR8KiIoSm4zdUw")
    videos = extract_videos_from_rss_feed(rss_feed)
    for video in videos:
        print(
            f"{video.title} - {video.video_id} - {'Short' if is_short(video.video_id) else 'Video'}"
        )
