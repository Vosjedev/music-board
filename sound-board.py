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
    import argparse
    
    def KeyInput(ArgSampleDir):
        if ArgSampleDir==None:
            while True:
                print("Where are your samples located?")
                SampleDir=prompt(" > ",completer=PathCompleter())
                if not isdir(SampleDir):
                    print(f"'{SampleDir}' is not a directory... Please enter a valid directory path")
                else:
                    break
        else:
            if not isdir(ArgSampleDir):
                print(f"'{ArgSampleDir}': Directory Not Found: Please enter a valid directory.")
            SampleDir=ArgSampleDir
            
        chdir(SampleDir)
        print("changed directory to '"+SampleDir+"'")

        print("starting keyserver.py...")
        e=keyserver.run()
        if not e==0:
            print("keyserver.py exited with value",e)
        exit(e)
    
    def ScriptInput(file,SampleDir,arg):
        from scripting.interpreter import interpret
        interpret(file=file,samples=SampleDir,arg=arg)
    
    parser=argparse.ArgumentParser(
            prog="sound-board"
            # epilog="""\n
            # [1]\n
            # see scripting.md on how to make a script file, and program a song.\n
            # [2]\n
            # see Samples.md on how to make a sample directory.\n
            # """
        )
    TypeFile=argparse.FileType(mode="r")
    parser.add_argument("-f","--file",type=TypeFile,metavar="scriptfile",      default=None, help="a file for scripting. See scripting.md for help.")
    parser.add_argument("-d","--dir", type=str,     metavar="sample-directory",default=None, help="Your directory of samples. See samples.md for help")
    parser.add_argument("-x",         action="store_true",                     default=False,help="echo script lines when using --file")
    parser.add_argument("-q",         action="store_true",                     default=False,help="be more silent when using --file")
    parser.add_argument("-Q",         action="store_true",                     default=False,help="be completely silent on stdout when using --file")
    

    arg=parser.parse_args()
    if arg.file==None:
        KeyInput(ArgSampleDir=arg.dir)
    else:
        if not isdir(arg.dir):
            print(f"'{arg.dir}': Directory Not Found: Please enter a valid directory.")
        ScriptInput(arg.file.name,arg.dir,arg)



if __file__.endswith("sound-board.py"):
    main()
