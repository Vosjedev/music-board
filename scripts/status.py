"""
This file print a statusbar when called.
"""










def r(left='',mid='',right=''):
    from os import get_terminal_size
    
    cols,lines=get_terminal_size()

    lsep=" "*int((cols/2)-len(left)-len(mid)/2)
    rsep=" "*int((cols/2)-len(right)-(len(mid)-len(mid)/2)-1)
    
    line=left+lsep+mid+rsep+right
    print(f"\0337\033[{lines};1H\033[30;47m{line}\033[0m\0338",end='',flush=True)