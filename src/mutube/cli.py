from .auth import initialize_youtube_client
from .utils import (
    console,
    format_number,
    decode_html_entities,
    format_date,
    parse_youtube_url,
)
from rich.table import Table
from .video import find_nearby_videos
import click
from .config import set_api_key


@click.group()
def cli():
    pass


@cli.command()
@click.argument("api_key")
def key(api_key):
    """Set your YouTube API key.

    API_KEY: Your YouTube Data API v3 key
    """
    set_api_key(api_key)
    console.print("[green]YouTube API key has been set successfully![/green]")


@cli.command()
@click.argument("url")
def analyze(url):
    video_id = parse_youtube_url(url)
    youtube = initialize_youtube_client()

    videos = find_nearby_videos(youtube, video_id)
    sorted_videos = sorted(
        videos, key=lambda x: int(x["statistics"]["viewCount"]), reverse=True
    )

    table = Table(
        show_header=True,
        show_footer=True,
        header_style="bold #bababa",
        footer_style="bold #bababa",
    )
    average_views = format_number(
        sum([int(video["statistics"]["viewCount"]) for video in videos]) / len(videos)
    )

    table.add_column("Ranking", style="#0c97c9", footer="Average", justify="left")
    table.add_column("Title", style="#fa5ca1", footer="", justify="left")
    table.add_column("Views", style="#1ce85d", footer=average_views, justify="right")
    table.add_column("Date", style="#fc8844", footer="", justify="right")

    for sorted_video_idx in range(len(sorted_videos)):
        title = decode_html_entities(
            sorted_videos[sorted_video_idx]["snippet"]["title"]
        )
        date = sorted_videos[sorted_video_idx]["snippet"]["publishedAt"]
        if sorted_videos[sorted_video_idx]["id"]["videoId"] == video_id:
            table.add_row(
                f"{sorted_video_idx + 1}",
                title,
                f"{format_number(int(sorted_videos[sorted_video_idx]['statistics']['viewCount']))}",
                format_date(date),
                style="bold white",
            )
        else:
            table.add_row(
                f"{sorted_video_idx + 1}",
                title,
                f"{format_number(int(sorted_videos[sorted_video_idx]['statistics']['viewCount']))}",
                format_date(date),
            )

    console.print(table)


def main():
    cli()


if __name__ == "__main__":
    main()
