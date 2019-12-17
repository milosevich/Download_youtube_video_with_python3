from pytube import YouTube
da = input('Enter link: ')
yt = YouTube(da).streams.first().download()