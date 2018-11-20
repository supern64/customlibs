# YTFinder
# A simple module to find YouTube Videos (https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video)
# IMPORTANT NOTE : VIDEO ID LENGTHS CAN CHANGE OVER TIME.

import urllib.request
import urllib.parse
import re
import youtube_dl

def getvideos(term):
    """Returns a list object of videos that matches the term."""
    query_string = urllib.parse.urlencode({"search_query" : term})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    if len(search_results) == 0:
        raise VideoNotFound("No videos found.")
    results = []
    for x in search_results:
        if 'http://www.youtube.com/watch?v=' + x in results:
            pass
        else:
            results.append('http://www.youtube.com/watch?v=' + x)
    return results

def getvideo(term):
    """Gets a single video and returns a string with the video's URL"""
    query_string = urllib.parse.urlencode({"search_query" : term})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    if len(search_results) == 0:
        raise VideoNotFound("No videos found.")
    return 'http://www.youtube.com/watch?v=' + search_results[0]

def getaudiourl(url):
    """
    Gets a audio URL of most Youtube videos.
    NOTE: THIS URL CAN BE UNSTABLE, KEEP IN MIND
    """
    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['formats'][0]['url']
    
def getvideourl(url):
    """
    Gets the REAL video URL of a Youtube video.
    NOTE: THIS URL CAN BE UNSTABLE, KEEP IN MIND
    """
    ydl_opts = {
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['formats'][19]['url']
class VideoNotFound(Exception):
    """Exception class when video is not found."""
    pass
