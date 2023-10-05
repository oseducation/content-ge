from googleapiclient.discovery import build
import json
import re
from isodate import parse_duration
from youtube_transcript_api import YouTubeTranscriptApi


youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_id(username):
    request = youtube.channels().list(
        part='id',
        forUsername=username
    )
    response = request.execute()
    channel = response['items'][0]
    return channel['id']

# channel_id = get_channel_id('@ycombinator')

channel_id = 'UCcefcZRL2oaA_uBNeo5UOWg'

def get_all_videos(channel_id):
    all_videos = []
    next_page_token = None
    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,  # Maximum allowed by API
            pageToken=next_page_token,
            type='video'
        )
        response = request.execute()
        videos = response.get('items', [])
        all_videos.extend(videos)
        next_page_token = response.get('nextPageToken')
        if next_page_token is None:
            break
    return all_videos

def save_to_json(videos, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)

def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )
    response = request.execute()
    item = response['items'][0]
    published_at = item['snippet']['publishedAt']
    duration_str = item['contentDetails']['duration']
    duration = parse_duration(duration_str)
    description = item['snippet']['description']
    return published_at, duration.total_seconds(), description


def extract_chapters(description):
    # Regex to match timestamps like 00:00 or 1:00:00
    pattern = re.compile(r'(\d+:\d+(:\d+)?) - (.+)')
    chapters = pattern.findall(description)
    chaps = []
    for chapter in chapters:
        chaps.append({
            "start": chapter[0],
            "name": chapter[2]
        })
    return chaps

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def populate_with_details(data):
    newData = []
    for video in data:
        id = video['id']['videoId']
        published_at, duration, description = get_video_details(id)
        newData.append({
            "id": id,
            "title": video['snippet']['title'],
            "published_at": published_at,
            "duration": duration,
            "description": description
        })
    return newData

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred: {e}")
        return ''
    
def populate_with_transcript(videos):
    for video in videos:
        transcript = get_transcript(video["id"])
        video["transcript"] = transcript
    return videos

def populate_with_chapters(videos):
    for video in videos:
        if video["duration"] < 300:
            video["chapters"] = []
        else:
            video["chapters"] = extract_chapters(video["description"])


videos = get_all_videos(channel_id)
videos = populate_with_details(videos)
populate_with_transcript(videos)
populate_with_chapters(videos)
save_to_json(videos, 'videos5.json')

