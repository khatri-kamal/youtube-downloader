# Additional Feature I want to add is to download the videos in correct folder based on 
# title of the video. If its a workout then I want in workout folder, if its a movie then movie and so on.
# Basic way I though of is. 
# use different list which holds strings that I could see if it matches the title and sort through that.
# First of have 3 list with strings apporate to sort the downloaded vidoes.
# Use loop to go through all different list at once. 
# if the title of the vidoe matches the strings within array the sort them out. 
#This is not a perfect prohram, one of the main error is if a title of a video is like this 
# Projects/Projects then it will NOT save in project folder as there is no space seprating the words

from pytube import YouTube
from sys import argv

projects = ["project", "projects", "tutorial", "java", "python", "javascript", "teaching", "development"]

movies = ["movie", "full movies"]

flute = ["Flute", "bansuri"]

workout = ["meal plan", "diet", "bulk", "workout", "streching", "workout"]

videLinks = argv[1]
youtube = YouTube(videLinks)

print("Title: ", youtube.title, "\nViews: ", youtube.views)

youtubeDownloads = youtube.streams.get_highest_resolution()

title_words = youtube.title.lower().split()

if any(word in title_words for word in workout):
    youtubeDownloads.download('/home/kamal/Videos/YouTube/workout')
    print("Downloaded Video is in Workout folder")

elif any(word in title_words for word in projects):
    youtubeDownloads.download('/home/kamal/Videos/YouTube/projects')
    print("Downloaded Video is in projects folder")

elif any(word in title_words for word in movies):
    youtubeDownloads.download('/home/kamal/Videos/YouTube/movie')
    print("Downloaded Video is in movie folder")

elif any(word in title_words for word in flute):
    youtubeDownloads.download('/home/kamal/Videos/YouTube/flute')
    print("Downloaded Video is in flute folder")

else:
    youtubeDownloads.download('/home/kamal/Videos/YouTube/Others')
    print("Downloaded Video is in Others folder")
