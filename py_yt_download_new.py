from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
url_link = input('Enter URL: ')
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url_link])
