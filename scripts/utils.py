"""
This file print a statusbar when called.
"""










import os

# find credits
def getcredits():
    from os.path import isfile
    if isfile("CREDITS"): # if a credits file exists:
        credits=open("CREDITS", 'r') # open CREDITS as read-only
        credits=credits.read() # read the file
        return credits

# screenresize
prev_cols=0;prev_lines=0
def applyscreenresize(credits):
    cols,lines=os.get_terminal_size() # get termsize
    if not cols==prev_cols or not lines==prev_lines: # if term resized:
        os.system("cls" if os.name=='nt' else "clear") # clear the screen
        print("CREDITS:\n"+credits) # print credits
        print("press escape twice to exit")
        prev_cols=cols;prev_lines=lines # store new size



# status
folder=os.getcwd()

def status(layer):
    left=f"layer: {layer}"
    right=f"folder: {folder}"
    __status(left)


def __status(left='',mid='',right=''):
    from os import get_terminal_size
    
    cols,lines=get_terminal_size()

    lsep=" "*int((cols/2)-len(left)-len(mid)/2)
    rsep=" "*int((cols/2)-len(right)-(len(mid)-len(mid)/2)-1)
    
    line=left+lsep+mid+rsep+right
    overflow=int(len(line)/cols)
    print(f"\0337\033[{lines-overflow};1H\033[30;47m{line}\033[0m\0338",end='',flush=True)