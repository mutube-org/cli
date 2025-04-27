from rich.console import Console
from datetime import datetime
import xmltodict
import html


def convert_xml_to_json(xml):
    return xmltodict.parse(xml)


def format_number(number):
    return f"{int(number):,}"


def decode_html_entities(text):
    return html.unescape(text)


def format_date(date):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d, %Y")


def parse_youtube_url(url):
    """
    Extract the video ID from a YouTube URL.
    Supports formats:
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://www.youtube.com/watch?v=VIDEO_ID (with escaped characters)
    - https://www.youtube.com/shorts/VIDEO_ID
    """
    # Handle youtu.be format
    if "youtu.be" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    
    # Handle shorts format
    if "shorts" in url:
        raise ValueError("Shorts are not supported for analyze")
        # return url.split("shorts/")[1].split("?")[0]
    
    # Handle watch format (both escaped and unescaped)
    if "watch" in url:
        # Split by either ?v= or \?v\=
        parts = url.split("?v=") if "?v=" in url else url.split("\\?v\\=")
        if len(parts) > 1:
            return parts[1].split("&")[0].split("?")[0]
    
    raise ValueError("Invalid YouTube URL")

console = Console()
