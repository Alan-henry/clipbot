from pytube import YouTube
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os


def edit():
    type=input("1 for vertically stacked 2 for normal : ")
    if(type=="1"):
        clip_link = input("Enter the link to the clip : ")
        bg_link=input("Enter the link for the background video : ")
        start=input("Enter starting point : ")
        end=input("Enter end point : ")
        YouTube(clip_link).streams.filter(file_extension="mp4").filter(res="720p").first().download()
        YouTube(bg_link).streams.filter(file_extension="mp4").filter(res="720p").first().download()

        clip_name=YouTube(clip_link).title+".mp4"
        bg_name=YouTube(bg_link).title+".mp4"
        try:
            os.rename(clip_name,"clip.mp4")
            os.rename(bg_name,"bg.mp4")
        except:
            os.remove("clip.mp4")
            os.remove("bg.mp4")
            os.rename(clip_name,"clip.mp4")
            os.rename(bg_name,"bg.mp4")
        clip=VideoFileClip("clip.mp4").subclip(int(start),int(end))
        bg_clip=VideoFileClip("bg.mp4").subclip(int(start),int(end))
        bg_audio= AudioFileClip("clip.mp4").subclip(int(start),int(end))
        combined= clips_array([[clip],[bg_clip]])
        combined.audio=CompositeAudioClip([bg_audio])
        combined=combined.resize(height=1920)
        final=combined
        # final=combined.crop(x1=2233.2,y1=0,x2=4493.2,y2=1920)
        final.write_videofile("final.mp4")

    if type=="2":
        clip_link=input("Enter the link of the clip : ")
        start=input("Enter starting point : ")
        end=input("Enter end point : ")
        YouTube(clip_link).streams.filter(file_extension="mp4").filter(res="720p").first().download()
        clip_name=YouTube(clip_link).title+".mp4"

        try:
            os.rename(clip_name,"clip.mp4")
        except:
            os.remove("clip.mp4")
            os.rename(clip_name,"clip.mp4")

        clip=VideoFileClip("clip.mp4").subclip(int(start),int(end))
        clip=clip.resize(height=1920)
        final=clip.crop(x1=1116.6,y1=0,x2=2246.6,y2=1920)
        final.write_videofile("final.mp4")

        
    
edit()

        
