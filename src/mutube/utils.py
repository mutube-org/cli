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
    Extract the video ID from a YouTube URL
    """
    if "shorts" in url:
        return url.split("shorts/")[1]
    elif "watch" in url:
        return url.split("watch?v=")[1]
    else:
        raise ValueError("Invalid YouTube URL")


console = Console()
