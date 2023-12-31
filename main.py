import pytube, os
from prettytable import PrettyTable
from pytube.cli import on_progress

def main():
    os.system("cls")
    link = input("Please paste the youtube link here: ")
    yvideo = pytube.YouTube(url=link, on_progress_callback=on_progress)
    yvideo.check_availability()
    print(f"\n{yvideo.title}\n")
    print("1 -> just audio\n2 -> video with no sound\n3 -> video with sound\n")
    while True:
        try:
            choice = int(input("What number do you choose ? "))
            if choice in range(1, 4):
                break
            else:
                print("Invalid number")
        except ValueError:
            print("This is not a number")
    
    print("Getting Data ..")
    if get_data(yvideo.streams, choice):
        print(":)\nDownload complete\nFind the downloaded file in the same folder of this app.")
    else:
        print("Apologies, an error occurred")
    os.system("pause")
    

def get_data(streams, choice: int) -> bool:    
    if choice == 1: 
        data = PrettyTable(["itag", "mime_type", "bitrate", "size (MB)"])
        for stream in streams.filter(only_audio=True).order_by("abr").desc():
            data.add_row([stream.itag, stream.mime_type, stream.abr, stream.filesize_mb])
        print(data)
    elif choice == 2:
        data = PrettyTable(["itag", "mime_type", "resolution", "fps", "size (MB)"])
        for stream in streams.filter(only_video=True).order_by("resolution").desc():
            data.add_row([stream.itag, stream.mime_type, stream.resolution, stream.fps, stream.filesize_mb])
        print(data)
    elif choice == 3:
        data = PrettyTable(["itag", "mime_type", "resolution", "fps", "size (MB)"])
        # first I'll try no to use ffmpeg
        # just show the progressive tracks only
        for stream in streams.filter(progressive=True).order_by("resolution").desc():
            data.add_row([stream.itag, stream.mime_type, stream.resolution, stream.fps, stream.filesize_mb])
        print(data)
        

    done = False
    while not done:
        try:
            itag = int(input("Enter the itag of the chosen format: "))
            chosen = streams.get_by_itag(itag)
            assert chosen is not None
            print("Downloading ..")
            chosen.download(filename=chosen.default_filename)
        except ValueError:
            print("This is not a number")
        except AssertionError:
            print("This itag does not exist")
        else:
            done = True
    
    return done

main()

'''random thoughts:
pyscript
GUI
cmd - no colors .. why ?
install ffmpeg for the user before running
config.json file for your app
make the app open itself in maximized window
I need to make much more apps than this - one per week
'''

# TODO: merge the audio and video
# TODO: make it verbose or simple (choice)