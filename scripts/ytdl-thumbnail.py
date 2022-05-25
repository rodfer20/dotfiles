# Requirements
# - ytdl
# - pafy


import pafy

url = "https://www.youtube.com/watch?v=oCdaOLmKu6s"
video = pafy.new(url) 
value = video.thumb
print("Thumbnail : " + value)
