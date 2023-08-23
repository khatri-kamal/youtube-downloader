from pytube import YouTube
from sys import argv

videLinks = argv[1]
youtube = YouTube(videLinks)

print("Title: ", youtube.title, "\nViews: ", youtube.views)

youtubeDownloads = youtube.streams.get_highest_resolution()

youtubeDownloads.download('/home/kamal/Videos/YouTube')