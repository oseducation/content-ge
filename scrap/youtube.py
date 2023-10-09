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
            video["chapters"] = [{
                "start": 0,
                "name": video["title"]
            }]
        else:
            video["chapters"] = extract_chapters(video["description"])

def filterVideosOld(videos):
    newVideos = []
    for video in videos:
        if len(video["chapters"]) > 0:
            newVideos.append(video)
        elif video["duration"] < 300:
            video["chapters"] = [{
                "start": 0,
                "name": video["title"]
            }]
            newVideos.append(video)
    return newVideos

def filterVideosOld(videos):
    newVideos = []
    for video in videos:
        if len(video["chapters"]) > 0:
            newVideos.append(video)
        elif video["duration"] < 300:
            video["chapters"] = [{
                "start": 0,
                "name": video["title"]
            }]
            newVideos.append(video)
    return newVideos

def getChapterText(video, start, finish):
    transcript = video["transcript"]
    text = ''
    for snippet in transcript:
        if float(snippet["start"]) >= start and float(snippet["start"]) + float(snippet["duration"]) <= finish:
            text += snippet["text"] + ' '
    return text

def time_to_seconds(time_string):
    if type(time_string) is int:
        return time_string
    # Split the time string into hours, minutes, and (optionally) seconds
    time_segments = list(map(int, time_string.split(':')))
    # Calculate total seconds based on the number of segments
    if len(time_segments) == 2:  # HH:MM format
        minutes, seconds = time_segments
        hours = 0
    elif len(time_segments) == 3:  # HH:MM:SS format
        hours, minutes, seconds = time_segments
    else:
        raise ValueError("Invalid time format. Please use 'HH:MM' or 'HH:MM:SS'.")
    # Convert hours and minutes to seconds and add to the seconds value
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def getChapters(videos):
    chapters = []
    for video in videos:
        videoChapters = video["chapters"]
        for i in range(len(videoChapters)-1):
            text = getChapterText(video, time_to_seconds(videoChapters[i]["start"]), time_to_seconds(videoChapters[i+1]["start"]))
            chapters.append({
                "start": time_to_seconds(videoChapters[i]["start"]),
                "end": time_to_seconds(videoChapters[i+1]["start"]),
                "video_id": video["id"],
                "video_title": video["title"],
                "video_description": video["description"],
                "published_at": video["published_at"],
                "text": text,
                "name": videoChapters[i]["name"]
            })
        text = getChapterText(video, time_to_seconds(videoChapters[-1]["start"]), 1000000)
        chapters.append({
            "start": time_to_seconds(videoChapters[-1]["start"]),
            "end": video["duration"],
            "video_id": video["id"],
            "video_title": video["title"],
            "video_description": video["description"],
            "published_at": video["published_at"],
            "text": text,
            "name": videoChapters[-1]["name"]
        })
    return chapters

def populateVideosWithText(videos):
    newVideos = []
    for video in videos:
        text = getChapterText(video, 0, 10000000)
        newVideos.append({
            "video_id": video["id"],
            "video_title": video["title"],
            "video_description": video["description"],
            "published_at": video["published_at"],
            "text": text,
        })
    return newVideos



videos = get_all_videos(channel_id)
videos = populate_with_details(videos)
populate_with_transcript(videos)
populate_with_chapters(videos)
save_to_json(videos, 'videos5.json')

for video in videos:
    chapters = video["chapters"]
    if len(chapters) == 0:
        print(video)
    if type(chapters) is not list:
        video["chapters"] = [video["chapters"]]


with open('filename.json', 'w', encoding='utf-8') as f:
    json.dump(nx, f, ensure_ascii=False, indent=4)

ny = []
for video in nx:
    if video["video_id"] in videoIDs:
        ny.append(video)