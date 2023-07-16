
# idea board

## 1. A client/server model:

**the server:**
 - start a server
 - get key input
 - send input via "socket"
 
Socket Ideas:
 - just a tcp socket
 - custom socket made of a plain text file

**The client:**
 - listen to keyserver.py's socket
 - look if the file corresponding to that key exists
 - use playsound in a thread to start playing the sound.
 
Every client has a different instrument. The reason for the server and client being seperated processes/threads has the advantage of being able
to play multiple instruments/filesgroeps at the same time by connecting multiple clients to one keyserver.

