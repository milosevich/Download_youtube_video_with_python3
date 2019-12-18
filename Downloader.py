from pytube import YouTube, Playlist

def download_video(yt):
    print('Downloading video...')
    print(((YouTube(yt)).title))
    YouTube(yt).streams.first().download()

def download_playlist(url_link):
    pl = Playlist(url_link)
    n=1
    pl.populate_video_urls()
    urls = pl.video_urls
    length = (len(pl.video_urls))
    for url in urls:
        print('------------------------------------')
        print(f'Video {str(n)} out of {str(length)}')
        download_video (url)
        n=n+1  
    
def main():
    url_link = input('Enter URL: ')
    if '&list=' in url_link:
        download_playlist(url_link)
    else:
        download_video(url_link)
    print('Finished downloading.')
    input("Press enter to close program")

main()