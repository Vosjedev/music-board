"""
This file is imported by keyserver.py and run directly after reading a key.
It is run in a thread.
"""









from os.path import isfile
import threading
from playsound import playsound

def KeyToSample(key,layer):
    fname=f"layer{layer}/{key}" # compose a path using the layer number and the input letter
    # see if the file exists.
    if isfile(f"{fname}.mp3"): # mp3
        playsound(f"{fname}.mp3")
    elif isfile(f"{fname}.MP3"): # sometimes mp3 extention is MP3
        playsound(f"{fname}.MP3")
    elif isfile(f"{fname}.wav"): # wav
        playsound(f"{fname}.wav")
    elif isfile(f"{fname}.WAV"): # sometimes wav extention is WAV
        playsound(f"{fname}.WAV")

def KeyToLayer(i,layer):
    if i=="left" or i=="down":
        layer=layer-1
        if layer<1:
            layer=1
    elif i=="right" or i=="up":
        layer=layer+1
        if layer>12:
            layer=12
    elif i.startswith("f") and not i=="f":
        f=i[1:]
        layer=int(f)
    return layer