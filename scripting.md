# scripting playback

This file is documentation on scripting.
If you want to make a song using a text file and this program, this is where you want to be.

## the concept
To start, lets explore the concept. If you are already familiar with a shell-language like bash, skip to **using commands**.
First, go to the directory where sound-board is installed. Then, make a new text file. Be sure to make a .txt file, not a word file. In windows, you can do this by right-clicking in the directory, hovering over `new`, and clicking `Text file`. Give it the name `example-script`, and press enter. Now open it. Paste the following code into it:

```shell
# example script
play 1 A
waitsec .5
play 1 W
waitsec .5
play 1 S
waitsec .5
play 1 D
waitsec .5
play 1 F
waitsec .5
play 1 G

```

and save it using control-s. Now open a terminal in that directory (by clicking the path above the folder view, and typing `cmd` when using windows). Now run the playback file by using this command:

```shell
python3 sound-board.py --dir samples/piano/ --file example-script.txt
```

If you are in the correct directory, you should see the following appear in the terminal, together with some piano notes playing:

```
opening file...
reading file to memory...
preparing copy...
counting lines...
14
entering sample directory 'samples/piano/'
now in /SD/workbench/music-board/samples/piano
preparing last things...
starting playback
 1/14: comment
 2/14: comment
 3/14: playing layer1/A
 4/14: waiting 0.5 seconds
 5/14: playing layer1/W
 6/14: waiting 0.5 seconds
 7/14: playing layer1/S
 8/14: waiting 0.5 seconds
 9/14: playing layer1/D
10/14: waiting 0.5 seconds
11/14: playing layer1/F
12/14: waiting 0.5 seconds
13/14: playing layer1/G
14/14: line empty
```

Now let's break down the file.
Switch back to your text-file window.
In here, you see the words `play` and `waitsec` used a lot. Those are commands. They start an action. They make their request more specific using arguments, the words after the command. All arguments are seperated by spaces.
If a line starts with a `#`, it is a comment. A line starting with `#` will be ignored.

## using commands
For those who skipped the above:  
*You can run a script file using:*
```shell
python3 sound-board.py --dir path/to/sample/dir --file path/to/script-file.txt
```
*I recommend still following the instructions, as I will be explaining from the environment we set up there. You can skip the theory, as you already know how to use shell languages.*

**For everyone again**
### play
`play` is used for playing notes. It should be followed by two arguments. The first one is the layer, the second one the sample.
```shell
play 1 A
```
The example above will ask to play the sample bound to key A from layer 1.
```shell
play 6 B
```
The example above will ask to play the sample bound to key B from layer 6.

The letter is the key you would press to activate the sample. It is therefore also the filename of the sample, minus the extention (.mp3, .wav).

You can also give one argument, but it should be a mapping. See `map` command for more info.

Exercise:
In your example script, reverse the order of the letters, to make the notes go from highest to lowest. Run the script again, using the command I provided earlier.

### waitsec
`waitsec` is used to wait an number of seconds before running the next command. This can be any number you want. `waitsec` accepts one argument: the number of seconds to wait.
```shell
waitsec 1
```
The example above waits one second.
```shell
waitsec 0.5
```
The example above waits half a second. You could also type `waitsec .5`, that works as well.

### map
`map` is used to map a word to a sample. It has 3 arguments. These are `key`, `layer`, `sample`.

```shell
map a3 3 a
```
This example maps `a3` to sample a from layer 3.
After mapping something, you can use the mapping in `play` instead of a key and a layer:
```shell
play a3
```
will look up the key and layer by searching for alias `a3`.
This is usefull if you are a muzician, and want to map the names of the notes to the keys you would press in interactive mode.

It is also usefull to map sounds to there keys.
for example, if a dog barking once is on key f from layer 6, you can use this to map and play a bark:
```shell
map bark 6 f
# ...
play bark
# ...
```
