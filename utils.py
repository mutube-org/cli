from rich.console import Console
from datetime import datetime
import xmltodict
import html

def convert_xml_to_json(xml):
    return xmltodict.parse(xml)

def format_number(number):
    """
    Format a number to a string with commas and removes decimals
    """
    return f"{int(number):,}"

def decode_html_entities(text):
    """
    Decode HTML entities in text (e.g., &#39; to ')
    """
    return html.unescape(text)

def format_date(date):
    """
    Format a date to a string with the month and day
    """
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d, %Y")

def parse_youtube_url(url):
    """
    Extract the video ID from a YouTube URL
    """
    if "shorts" in url:
        return url.split("shorts/")[1]
    elif "watch" in url:
        return url.split("watch?v=")[1]
    else:
        raise ValueError("Invalid YouTube URL")

console = Console()

if __name__ == "__main__":
    EXAMPLE_SHORT_URL = "https://www.youtube.com/shorts/uQj5O4GTWtA"
    EXAMPLE_VIDEO_URL = "https://www.youtube.com/watch?v=gGQlY9NbLaI"
    print(parse_youtube_url(EXAMPLE_SHORT_URL))
    print(parse_youtube_url(EXAMPLE_VIDEO_URL))