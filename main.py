from json_reader import JSONReader as jsonR
from mp3_downloader import MP3Downloader as mp3Downloader
from load_env_paths import EnvPathLoader as envPathLoader
import os

VIDEO_LIST_PATH = os.getcwd()+'\\video_list.json'


def main():
    envPathLoader.load_env_paths()

    print('path:',VIDEO_LIST_PATH)
    video_data = jsonR.read_from_file(VIDEO_LIST_PATH)
    print(video_data)
    for group in video_data['groups']:
        print(group)
        print(group['group_video_list'])
        mp3Downloader.download_videos(directory_path="./songs/"+group['group_name'],video_list=group['group_video_list'])


if __name__ == '__main__':
    main()