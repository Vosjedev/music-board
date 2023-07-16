"""
This file is responsible for getting key input and notifying any connected clients when input is recieved.
ToDo:
 ( ) get key input
 ( ) Check if a file exists called {key}.mp3 or {key}.wav in {instumentdir} (which should be current directory)
 ( ) if above is true, play the file using playsound()
 
Issues:
 ( ) if a key is held, the sample is started repeatedly over and over again 
 
"""


def run():
    import os,sys,threading
    from os.path import isfile
    from scripts import input
    GetKeys=input.GetKeys
    try:
        from playsound import playsound
    except ModuleNotFoundError:
        print("installing playsound using pip")
        cmd="python3 -m pip install playsound"
        print(cmd)
        e=os.system(cmd)
        if e==0:
            from playsound import playsound
        else:
            print("command",cmd,"failed with code",str(e)+", assuming playsound did not install correctly.")
            print("If you think it did install correctly, please run me again, and this should not happen anymore.")
            print("Exiting now with code 255.")
            return 255

    print("press escape twice to exit")
    while True:
        skip=False # set skip to false
        i=GetKeys() # read one letter
        if i=='escape':
            print("You pressed escape twice, exiting...")
            return 0
        # see if the file exists.
        if isfile(f"{i}.mp3"): # mp3
            sound=threading.Thread(target=playsound,args=[f"{i}.mp3"],daemon=True)
        elif isfile(f"{i}.MP3"): # sometimes mp3 extention is MP3
            sound=threading.Thread(target=playsound,args=[f"{i}.MP3"],daemon=True)
        elif isfile(f"{i}.wav"): # wav
            sound=threading.Thread(target=playsound,args=[f"{i}.wav"],daemon=True)
        elif isfile(f"{i}.WAV"): # sometimes wav extention is WAV
            sound=threading.Thread(target=playsound,args=[f"{i}.WAV"],daemon=True)
        else:
            skip=True # ask to skip starting the thread, as no new thread was made
        
        # sound.setDaemon(True) # to make it kill itself when the program closes. # already set in definition
        if not skip:
            sound.start() # start the thread
        
        
    
    