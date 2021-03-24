from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen import MutagenError
import glob
import argparse
import sys
import os

def delete_lyrics_of_mp3(MUSIC_PATH):
    try:
        tags = MP3(MUSIC_PATH)
        if 'USLT::eng' in tags:
            tags.pop('USLT::eng', None)
            tags.save()
            print('[Success] Delete lyrics of ' + MUSIC_PATH)
    except MutagenError:
        print('[Error] ' + MUSIC_PATH + ' is not found')
        sys.exit(1)

def delete_lyrics_of_mp4(MUSIC_PATH):
    try:
        tags = MP4(MUSIC_PATH)
        if '\xa9lyr' in tags:
            tags.pop('\xa9lyr', None)
            tags.save()
            print('[Success] Delete lyrics of ' + MUSIC_PATH)
    except MutagenError:
        print('[Error] ' + MUSIC_PATH + ' is not found')
        sys.exit(1)

def all_mp3(ITUNES_MEDIA_PATH):
    mp3_list = glob.glob(ITUNES_MEDIA_PATH + ('/' if ITUNES_MEDIA_PATH[-1] != '/' else '') + 'Music/**/*.mp3', recursive=True)
    for i in mp3_list:
        delete_lyrics_of_mp3(i)

def all_mp4(ITUNES_MEDIA_PATH):
    mp4_list = glob.glob(ITUNES_MEDIA_PATH + ('/' if ITUNES_MEDIA_PATH[-1] != '/' else '') + 'Music/**/*.m4a', recursive=True)
    for i in mp4_list:
        delete_lyrics_of_mp4(i)

def parse_args():
    parser = argparse.ArgumentParser(description='Delete lyrics of mp3, mp4 and m4a')
    parser.add_argument('--mp3', type=str, help='Delete lyrics of specified mp3')
    parser.add_argument('--mp4', type=str, help='Delete lyrics of specified mp4 or m4a')
    parser.add_argument('-f', '--folder', type=str, help='Delete lyrics of music in iTunes Media folder')

    args = parser.parse_args()
    return args

def main(args):
    if args.mp3 != None:
        delete_lyrics_of_mp3(args.mp3)
    if args.mp4 != None:
        delete_lyrics_of_mp4(args.mp4)
    if args.folder != None:
        if os.path.isdir(args.folder):
            all_mp3(args.folder)
            all_mp4(args.folder)
        else:
            print('[Error] ' + args.folder + ' is not found')
            sys.exit(1)

if __name__ == '__main__':
    main(parse_args())
