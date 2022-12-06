from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video")
  print("Download has completed!")

link = input("Youtube URL: ")
Download(link)