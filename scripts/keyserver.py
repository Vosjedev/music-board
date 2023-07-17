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
    import os,threading
    from scripts.input import GetKeys
    from scripts.utils import status, getcredits, applyscreenresize
    from scripts.keyToSample import KeyToSample, KeyToLayer

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
    
    
    layer=1 # set layer to 1
    credits=getcredits()
    
    while True:
        
        applyscreenresize(credits=credits)
        status(layer)
        
        skip=False # set skip to false
        i=GetKeys() # read one letter
        i=str(i)
        
        KeyToSampleThread=threading.Thread(target=KeyToSample,args=[i,layer])
        if i=='escape': # exit
            # no point of putting this in a function
            print("You pressed escape twice, exiting...")
            return 0 # return exit code of 0
        
        layer=KeyToLayer(i,layer) # see if layer needs to be adjusted
        
        if i=="up" or i=="down" or i=="left" or i=="right" or i=="pause" or i=="break" or i=="insert" or i=="delete" or i=="escape":
            skip=True
        
        if not skip:
            KeyToSampleThread.start() # start the thread
        
        
    
    