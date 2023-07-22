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
    printerr(f"\033[0;41mSyntax error on line {linenr}\033[0;31m\n> \033[0;40m{line}\n\033[0;48;31mError: {error}\033[0m")

def printerr(msg,end='\n',flush=True): # print for stderr
    from sys import stderr
    stderr.write(f"{msg}{end}")
    if flush:
        stderr.flush()

def interpret(file,samples,arg):
    
    def print(msg,end='\n',flush=True,skipq=False):
        # set print, because python unsets it, because it thinks
        # it is defined, but is is only defined when -Q flag given
        # I wrote this myself, it is not the original function,
        # it is only a recreation I made.
        from sys import stdout
        stdout.write(f"{msg}{end}")
        if flush:
            stdout.flush()
        
    if arg.Q or arg.q: # if silent on:
        oldprint=print
        def print(msg,end='\n',flush=True,skipq=False): # overwrite print function
            if skipq and not arg.Q: # if it wants to skip -q:
                oldprint(msg=msg,end=end,flush=flush) # only then print it.
    
    import os,colorama,threading
    colorama.init()
    from scripts.keyToSample import KeyToSample
    from time import sleep
    from scripting.translation import map
    
    print("opening file...")
    scriptfile=open(file,"r") # open readonly
    print("reading file to memory...")
    scriptcontent=scriptfile.read() # read to var
    print("closing file on disk...")
    scriptfile.close()
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
    # print(f"now in {os.getcwd()}")
    print('preparing last things...')
    printinfo=printinfoclass() # set printinfo class
    printinfo.argx=arg.x # pass some arguments to printinfo class
    printinfo.argq=arg.q
    printinfo.argQ=arg.Q
    
    mappings=map()
    
    previousaction=['','','']
    MappedSuccessfull=False
    MappedCnt=0
    
    print("starting playback")
    cnt=0
    for line in script:
        cnt=cnt+1 # up line counter
        
        action=line.split(' ') # split line arguments on space
        
        while '' in action: # remove all empty arguments from action
            action.remove('')
        
        try:
            actioncmd=action[0]
        except IndexError:
            actioncmd="None"
        
        if MappedSuccessfull: # print stuff for map command
            MappedCnt=MappedCnt+1
            
            if previousaction[0]=="map" and actioncmd=="map": # if previous action and current action are map,
                print("\r",end='',flush=True) # overwrite previous line
            else: # else
                if MappedCnt==1:
                    printinfo.pr(f"mapped {previousaction[1]} to {previousaction[2]}/{previousaction[3]}") # print the info of the mapping as map doesn't do that
                else:
                    printinfo.pr(f"mapped {MappedCnt} mappings")
        else:
            MappedCnt=0
        MappedSuccessfull=False

        prefix=" "*int(len(str(total))-len(str(cnt))) # calculate the amount of spaces before line number
        if arg.x:
            print(f"{prefix}{cnt}/{total} > {line}") # print line if enabled
        elif arg.q: # if almost silent:
            print(f"action {prefix}{cnt}/{total}, {round(100/(total/cnt))}%\r",end='',flush=True,skipq=True) # print line number, and prepare for overwriting with next line number
        else:
            print(f"{prefix}{cnt}/{total}: ",end='',flush=True) # otherwise only print progress, to add more later
        
        if len(action)<=0: # if line is empty
            printinfo.pr("line empty")
        elif str(action[0]).startswith("#"): # if line is comment
            printinfo.pr("comment")
        
        # commands
        elif action[0]=="play":
            dontplay=False
            if len(action)<2: # if line does not have enough arguments, print syntaxerror
                syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected between 1 and 2, got {len(action)-1}")
            else:
                if len(action)>=3:
                    sample=str(action[2])
                    layer=str(action[1])
                else:
                    if len(str(action[1]))<=1: # check if the input has less than one characters. if so, it is not a mapping, as mapping must be 2+ characters lone
                        syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected 2, got {len(action)-1}\nIf you tried to use a mapping called {action[1]}, this is not possible. Mappings must be more than 1 characters long.")
                        dontplay=True
                    sample,layer=mappings.getmap(action[1])
                    if sample==None or layer==None:
                        syntaxerror(line=line,linenr=cnt,error=f"KeyError: Key {action[1]} not found.")
                        dontplay=True
                printinfo.pr(f"playing {layer}/{sample}")
                samplethread=threading.Thread(target=KeyToSample,args=(sample,layer))
                # KeyToSample(layer=str(action[1]),key=str(action[2])) # ask KeyToSample to play the note
                if not sample=="up" and not sample=="down" and not sample=="left" and not sample=="right" and not sample=="pause" and not sample=="break" and not sample=="insert" and not sample=="delete" and not sample=="escape":
                    if not dontplay: samplethread.start()
        
        elif action[0]=="waitsec":
            if len(action)<2: # if line does not have enough arguments, print syntaxerror
                syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected 1, got {len(action)-1}")
            # if not type(action[1])==int:
                
            else:
                try: # try for caching ValueErrors if the user used a non-float number as sleep time
                    time=float(action[1]) # convert from str to float
                    printinfo.pr(f"waiting {time} seconds")
                    sleep(time) # sleep the fiven time
                except ValueError: # print syntaxerror if argument was not a number (which returns VallueError)
                    syntaxerror(line=line,linenr=cnt,error=f"Wrong Type: expected a number, got something else")
        
        elif action[0]=="map":
            if len(action)<3: # if line does not have enough arguments, print syntaxerror
                syntaxerror(line=line,linenr=cnt,error=f"Not Enough Aguments: expected 2, got {len(action)-1}")
            elif len(str(action[1]))<=1:
                syntaxerror(line=line,linenr=cnt,error=f"Syntax Error: a mapping's name can't be one character long. Current name: {action[1]}")
            else:
                MappedSuccessfull=True
                mappings.map(key=action[1],layer=action[2],sample=action[3])
            # normaly we would have to print something for each action, but for mappings, this is handeled earlier.
                
                
                
        else: 
            syntaxerror(line=line,linenr=cnt,error=f"Command Not Found: '{action[0]}'")
        
        previousaction=action
    
    print("\ndone")
    print("exiting...")
            
        
        
    