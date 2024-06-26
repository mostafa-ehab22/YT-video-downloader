from pytube import YouTube
from sys import argv
"""
Running program: python YTDownloader.py "LINK"
"""

# Takes 1st line after program name & stores it as link
link = argv[1]
yt = YouTube(link)

print("Title:",yt.title)
print("Views:","{:,}".format(yt.views))

user_input = input("Do you want to download video? (y/n) ").strip().lower()

if user_input == 'y':
    # Getting Video Resolution
    resolution = yt.streams.filter(res="480p",progressive=True).first()

    # Checking if wanted resolution available
    if resolution:
        resolution.download("D:\Mostafa\YT Videos")
        print("Download Successfull!")
    else:
        print("Video Resolution not availabe")
