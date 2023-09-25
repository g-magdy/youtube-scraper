import pytube
from prettytable import PrettyTable

def main():
    link = "https://youtu.be/guhw4oX6jhs?si=s7PO9s8Z3wNbMM0P"
    yvideo = pytube.YouTube(url=link)
    yvideo.check_availability()
    streams = yvideo.streams.order_by("resolution")
    

def get_video(streams):
    data = PrettyTable(["itag", "type", "resolution", "fps", "size (MB)"])
    for stream in streams:
        data.add_row([stream.itag, stream.type, stream.resolution, stream.fps, stream.filesize_mb])

    print(data)

    done = False
    while not done:
        try:
            itag = int(input("Enter the itag of the chosen format: "))
            chosen = streams.get_by_itag(itag)
            assert chosen is not None
            chosen.download(filename=chosen.default_filename)
        except ValueError:
            print("This is not a number")
        except AssertionError:
            print("this itag does not exist")
        else:
            done = True

def get_audio(streams):
    audio = streams.get_audio_only()
    audio.download(filename=audio.default_filename)


main()

'''random thoughts:
pyscript
GUI
cmd - no colors .. why ?
install ffmpeg for the user before running
config.json file for your app
I need to make much more apps than this - one per week
'''

# TODO: don't ask for the name of the file
# TODO: pretty table
# TODO: get audio
# TODO: get video
# TODO: merge the audio and video

# audio = streams.get_audio_only()
# video = streams.get_highest_resolution()
# assert audio is not None
# assert video is not None
# print(audio.default_filename)
# print(video.default_filename)
# print(audio.filesize_mb)
# print(video.filesize_mb)
