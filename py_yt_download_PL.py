from pytube import Playlist
da = input('Enter link for playlist: ')
pl = Playlist(da)
pl.download_all()
