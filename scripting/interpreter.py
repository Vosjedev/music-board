"""
This file is an interpreter for script files.
It should open a file and read it to memory.
It should then iterate over the lines. It should send all notes to translation.py
for translating when enabled, and it should ask KeyToSample in keyToSample.py from
scripts directory to start the note.





"""


class printinfoclass:
    argx=False
    argq=False
    argQ=False
    def pr(self,msg=str):
        if self.argx==False and self.argq==False and self.argQ==False: # if -x not passed or silent on:
            print(msg) # print msg


def syntaxerror(linenr,line,error): # print syntaxerror function
    printerr(f"\033[0;41mSyntax error on line {linenr}\033[0;31m\n> {line}\nError: {error}\033[0m")

def printerr(msg,end='\n',flush=True): # print for stderr
    from sys import stderr
    stderr.write(f"{msg},{end}")
    if flush:
        stderr.flush()

printbackup=print # make a backup of print

def interpret(file,samples,arg):
    
    print=printbackup # set print back, because python unsets it, because it thinks
                      # it is defined, but is is only defined when -Q flag given
    if arg.Q: # if silent on:
        def print(msg,end='\n',flush=True): # overwrite print function
            pass # and make it do nothing
    
    import os,colorama,threading
    colorama.init()
    from scripts.keyToSample import KeyToSample
    from time import sleep
    
    print("opening file...")
    scriptfile=open(file,"r") # open readonly
    print("reading file to memory...")
    scriptcontent=scriptfile.read() # read to var
    print("preparing copy...")
    script=scriptcontent.split("\n") # split at line breaks to iterate over the lines
    print("counting lines...")
    cnt=0
    for line in script:
        cnt=cnt+1
        print(f"\r{cnt}",end='',flush=True)
    total=cnt
    print('')
    print(f"entering sample directory '{samples}'")
    os.chdir(samples)
    print(f"now in {os.getcwd()}")
    print('preparing last things...')
    printinfo=printinfoclass() # set printinfo class
    printinfo.argx=arg.x # pass some arguments to printinfo class
    printinfo.argq=arg.q
    printinfo.argQ=arg.Q

    print("starting playback")
    cnt=0
    for line in script:
        cnt=cnt+1 # up line counter
        prefix=" "*int(len(str(total))-len(str(cnt))) # calculate the amount of spaces before line number
        if arg.x:
            print(f"{prefix}{cnt}/{total} > {line}") # print line if enabled
        elif arg.q: # if almost silent:
            print(f"{prefix}{cnt}/{total}\r",end='',flush=True) # print line number, and prepare for overwriting with next line number
        else:
            print(f"{prefix}{cnt}/{total}: ",end='',flush=True) # otherwise only print progress, to add more later
        
        action=line.split(' ') # split line arguments on space
        if len(action)<=1: # if line is empty
            printinfo.pr("line empty")
        elif str(action[0]).startswith("#"): # if line is comment
            printinfo.pr("comment")
            
        elif action[0]=="play":
            if len(action)<3: # if line does not have enough arguments, print syntaxerror
                syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected 2, got {len(action)-1}")
            else:
                printinfo.pr(f"playing layer{action[1]}/{action[2]}")
                samplethread=threading.Thread(target=KeyToSample,args=(str(action[2]),str(action[1])))
                # KeyToSample(layer=str(action[1]),key=str(action[2])) # ask KeyToSample to play the note
                samplethread.start()
        
        elif action[0]=="waitsec":
            if len(action)<2: # if line does not have enough arguments, print syntaxerror
                syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected 1, got {len(action)-1}")
            # if not type(action[1])==int:
                
            else:
                try:
                    time=float(action[1])
                    print(f"waiting {time} seconds")
                    sleep(time)
                except ValueError:
                    syntaxerror(line=line,linenr=cnt,error=f"Wrong Type: expected a number, got something else")
            
        
        
    