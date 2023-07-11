"""
The idea of this file is the following:
 - listen to keyserver.py's socket
 - look if the file corresponding to that key exists
 - use playsound in a thread to start playing the sound.
 
Every client has a different instrument. The reason for the server and client being seperated processes/threads has the advantage of being able
to play multiple instruments/filesgroeps at the same time by connecting multiple clients to one keyserver.
"""



