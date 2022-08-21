from time import sleep
from pytube import YouTube
import re
from datetime import datetime, timedelta
import os

print(
    """######################################################\n"""
    """##                    YouDownMach                   ##\n"""
    """##          Execute in terminal and voilà :)        ##\n"""
    """##      https://github.com/FMachadoG/YouDownMach    ##\n"""
    """##          By: https://github.com/FMachadoG        ##\n"""
    """######################################################\n"""
    )

link = input(" - URL video: ")

linkCode = link.replace("https://www.youtube.com", "").replace("https://youtu.be", "")
validLink = re.match(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", linkCode)

if (link.__contains__('https://www.youtube.com') == False and link.__contains__('https://youtu.be') == False):
    print(f"Invalid URL!")
    
    exit()

elif validLink is None:
        print("Invalid CODE video!")
        
        exit()

yt = YouTube(link)
downVideo = input(" - Download video?(y/n): ")

if not (downVideo == 'y' or downVideo == 'n'):
    print("Invalid answer! Please enter 'y'(yes) or 'n'(no).")
    
    exit()

downAudio = input(" - Download audio?(y/n): ")

if not (downAudio == 'y' or downAudio == 'n'):
    print("Invalid answer! Please enter 'y'(yes) or 'n'(no).")
    
    exit()

showInfo = input(" - Show video information?(y/n): ")

if not (showInfo == 'y' or showInfo == 'n'):
    print("Invalid answer! Please enter 'y'(yes) or 'n'(no).")
    
    exit()

if (downVideo == 'y' or downAudio == 'y'):
    print("\n########## DOWNLOADING ##########")

    pathDownload = input(" - Path to download: ")

    if os.path.exists(pathDownload) == False:
        print("Path not exist!")
        
        exit()

    if downVideo == 'y':
        resolVideo = input(" - Video resolution lowest or highest?(l/h)): ")

        if not (resolVideo == 'l' or resolVideo == 'h'):
            print("Invalid answer! Please enter 'l'(lowest)' or 'h'(highest).")
            
            exit()

        elif resolVideo == 'l':
            print("\n - Downloading video...")

            yVideo = yt.streams.get_lowest_resolution()
            yVideoTitle = yVideo.title.replace(".", "_")

            yVideo.download(pathDownload, f'{yVideoTitle}-YouDownMach.mp4')

            dateNow = datetime.now()
            print(f" - Done! - {dateNow.strftime('%d/%m/%Y %H:%M:%S')}")
            

        else:
            print("\n - Downloading video...")

            yVideo = yt.streams.get_highest_resolution()
            yVideoTitle = yVideo.title.replace(".", "_")

            yVideo.download(pathDownload, f'{yVideoTitle}-YouDownMach.mp4')

            dateNow = datetime.now()
            print(f" - Done! - {dateNow.strftime('%d/%m/%Y %H:%M:%S')}")
            

    if downAudio == 'y':
        print("\n - Downloading audio...")

        yAudio = yt.streams.get_audio_only("mp4")
        yAudioTitle = yAudio.title.replace(".", "_")

        yAudio.download(pathDownload, f'{yAudioTitle}-YouDownMach.mp3')

        dateNow = datetime.now()
        print(f" - Done! - {dateNow.strftime('%d/%m/%Y %H:%M:%S')}")
        

if showInfo == 'y':
    # OK
    viewsAmountVideo = "{:,}".format(yt.views)
    viewsAmountVideo = viewsAmountVideo.replace(",", ".")

    publiDateVideo = yt.publish_date
    publiDateVideo = publiDateVideo.strftime("%b %d, %Y")

    timeVideo = yt.length
    timeVideo = "{:0>8}".format(str(timedelta(seconds=timeVideo)))

    print("\n########## VIDEO INFORMATION ##########")

    print(f" - Title: --------- {yt.title}")
    print(f" - Views: --------- {viewsAmountVideo}")   
    print(f" - Publish date: -- {publiDateVideo}")
    print(f" - Author: -------- {yt.author}")
    print(f" - Time: ---------- {timeVideo}")
    print(f" - Channel: ------- {yt.channel_url}")
    print(f" - Thumb: --------- {yt.thumbnail_url}")

    # print(f" Descrip: {yt.description}")
    # print(f" Keywords: {yt.keywords}")
    # print(f" Channel ID: {yt.channel_id}")

    # JSON
    # print(yt.initial_data)
    # print(yt.streaming_data)
    # print(yt.vid_info)

    # print(yt.check_availability)
    # print(yt.bypass_age_gate)
    # print(yt.caption_tracks)
    # print(yt.captions)
    # print(yt.rating)
    # print(yt.metadata)
    # print(yt.register_on_complete_callback)
    # print(yt.register_on_progress_callback)
print("\n########################################\n")

