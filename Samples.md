# Sample folder Documentation

## making a sample folder
Steps:  
  
1. Make a new directory.
2. Place samples in there.
3. Make sure all that samples are in mp3 or wav format, and that there extentions are either mp3, wav, MP3, or WAV.
4. Make sure there are not other files in there than samples.
5. Rename every file to the key you want them on, plus the extention. If I would want `piano_A.mp3` under key `a`, I will call it `a.mp3`. You can put samples under any key. See the examples under here for special keys.
<br><br>

Examples:  
original filename | key I want it on | new filename
------------------|------------------|-----------------
`Piano_A.mp3`     |`a`               |`a.mp3`
`Piano_B.mp3`     |`s`               |`s.mp3`
`Piano_C.mp3`     |`d`               |`d.mp3`
`Guitar_A.mp3`    |`shift`-`a`       |`A.mp3`
`Guitar_B.mp3`    |`shift`-`s`       |`S.mp3`
`Guitar_C.mp3`    |`shift`-`d`       |`D.mp3`
`Syntesizer_A.mp3`|`control`-`a`     |`c-a.mp3`
`Syntesizer_B.mp3`|`control`-`s`     |`c-s.mp3`
`Syntesizer_C.mp3`|`control`-`d`     |`c-d.mp3`

<br>

Some keys can't be used:  
`delete`  
`pauze`  
`f1` to `f12`  
`esc`  
`insert`  
Arrow keys (`left` `right` `up` `down`)  
<br>

On windows, the following also can't be used:  
`'`  
`~`  
`shift`-`~` (```)  <br>
`shift`-`'` (`"`)  <br>
`shift`-`6` (`^`)  <br>
*Note: when you press one of these keys, input is temporarily blocked until you press another key. The sample bound to that other key won't play. See footnote[1] for more info.*  
  
Some keys give another key combination instead when pressed:  
*c means control here*  
key        | output
-----------|--------
`enter`    |`c-m`
`tab`      |`c-i`
`backspace`|`c-h`
  
<br><br>

Footnotes
[1]
When you press a key like `'` (this includes all charactes listed above), windows blocks input to wait for another key. If you then press `a` for example, the correct sample won't play, because the program receives `á` as input instead of `a`.

