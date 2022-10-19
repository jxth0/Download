import pytube 
url = input("ENTER URL:")
pytube.YouTube(url).streams.get_highest_resolution().download("Desktop")
print("Done")