import sys
import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL format")

def extract_metadata(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    title_tag = soup.find("meta", property="og:title")
    title = title_tag["content"] if title_tag else "Unknown Title"

    channel_tag = soup.find("link", itemprop="name")
    channel = channel_tag["content"] if channel_tag else "Unknown Channel"

    return title, channel

def download_thumbnail(video_id):
    image_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    try:
        img_data = requests.get(image_url).content
        with open('thumbnail.jpg', 'wb') as handler:
            handler.write(img_data)
    except requests.RequestException as e:
        print(f"Error downloading thumbnail: {e}")

def get_transcript(video_id):
    try:
        transcript_raw = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'es', 'de'])
        transcript_str_lst = [i['text'] for i in transcript_raw]
        return ' '.join(transcript_str_lst)
    except (TranscriptsDisabled, NoTranscriptFound):
        return "Transcript not available for this video."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_url>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    
    try:
        video_id = extract_video_id(youtube_url)
        title, channel = extract_metadata(youtube_url)
        transcript = get_transcript(video_id)
        download_thumbnail(video_id)
        
        print(f"Title: {title}")
        print(f"Channel: {channel}")
        print('=============')
        print(transcript)
    except Exception as e:
        print(f"Error: {e}")
