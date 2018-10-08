from __future__ import unicode_literals
import youtube_dl


class MP3Downloader:

    @staticmethod
    def download_videos(directory_path="",video_list=[]):
        if("" == directory_path):
            directory_path = "./"
        elif(not directory_path.endswith("/")):
            directory_path = directory_path + "/"
        ydl_opts = {
            'format': 'bestaudio/best',
            'download_archive': 'downloaded_songs.txt',
            'outtmpl': directory_path+'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(video_list)
