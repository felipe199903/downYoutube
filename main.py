from pytube import YouTube

def download(link):
  youtube_object = YouTube(link)
  youtube_object = youtube_object.streams.get_highest_resolution()

  try:
      youtube_object.download()
  except TypeError as e:
    raise TypeError("There has been an error in downloading your youtube video") from e

  print("Download has completed!")

link = input("Youtube URL: ")
download(link)