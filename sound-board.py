#!/usr/bin/python3

"""
This file should first let the user choose an instument/filegroep, then start the keyserver, and then start a client for every instument
selected.
"""







def main():
    # print("importing scripts...")
    from scripts import keyserver,client
    from os.path import isdir
    from os import chdir
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    
    while True:
        print("Where are your samples located?")
        SampleDir=prompt(" > ",completer=PathCompleter())
        if not isdir(SampleDir):
            print(f"'{SampleDir}' is not a directory... Please enter a valid directory path")
        else:
            break
    
    chdir(SampleDir)
    print("changed directory to '"+SampleDir+"'")
    
    print("starting keyserver.py...")
    e=keyserver.run()
    if not e==0:
        print("keyserver.py exited with value",e)
    exit(e)





if __file__.endswith("sound-board.py"):
    main()
