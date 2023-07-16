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
    from scripts import status
    GetKeys=input.GetKeys
    try: # import playsound
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
    try: # import colorama
        import colorama
    except ModuleNotFoundError:
        print("installing colorama using pip")
        cmd="python3 -m pip install colorama"
        print(cmd)
        e=os.system(cmd)
        if e==0:
            import colorama
        else:
            print("command",cmd,"failed with code",str(e)+", assuming playsound did not install correctly.")
            print("If you think it did install correctly, please run me again, and this should not happen anymore.")
            print("Exiting now with code 255.")
            return 255

    # sys.setrecursionlimit(sys.getrecursionlimit()+100)

    colorama.init()

    os.system("cls" if os.name=='nt' else "clear") # clear the screen
    
    if isfile("CREDITS"): # if a credits file exists:
        credits=open("CREDITS", 'r') # open CREDITS as read-only
        credits=credits.read() # read the file
        print("CREDITS:")
        print(credits) # print the file
    
    layer=1 # set layer to 1
    folder=os.getcwd()
    
    print("press escape twice to exit")
    while True:
        
        left=f"layer: {layer}"
        right=f"folder: {folder}"
        status.r(left=left,mid="|",right=right)
        
        skip=False # set skip to false
        i=GetKeys() # read one letter
        i=str(i)
        fname=f"layer{layer}/{i}" # compose a path using the layer number and the input letter
        # see if the file exists.
        if isfile(f"{fname}.mp3"): # mp3
            sound=threading.Thread(target=playsound,args=[f"{fname}.mp3"],daemon=True)
        elif isfile(f"{fname}.MP3"): # sometimes mp3 extention is MP3
            sound=threading.Thread(target=playsound,args=[f"{fname}.MP3"],daemon=True)
        elif isfile(f"{fname}.wav"): # wav
            sound=threading.Thread(target=playsound,args=[f"{fname}.wav"],daemon=True)
        elif isfile(f"{fname}.WAV"): # sometimes wav extention is WAV
            sound=threading.Thread(target=playsound,args=[f"{fname}.WAV"],daemon=True)
        else:
            skip=True # ask to skip starting the thread, as no new thread was made
        if i=='escape': # exit
            print("You pressed escape twice, exiting...")
            return 0 # return exit code of 0
        elif i=="left" or i=="down":
            layer=layer-1
            if layer<1:
                layer=1
        elif i=="right" or i=="up":
            layer=layer+1
            if layer>12:
                layer=12
        elif i.startswith("f") and not i=="f":
            skip=True
            f=i[1:]
            layer=int(f)
        
        if i=="up" or i=="down" or i=="left" or i=="right" or i=="pause" or i=="break" or i=="insert" or i=="delete" or i=="escape":
            skip=True
        
        # sound.setDaemon(True) # to make it kill itself when the program closes. # already set in definition
        if not skip:
            sound.start() # start the thread
        
        
    
    