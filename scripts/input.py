"""
This file is for reading input, one key at a time.
See
https://python-prompt-toolkit.readthedocs.io/en/stable/pages/asking_for_input.html#reading-keys-from-stdin-one-key-at-a-time-but-without-a-prompt
for the original script. I modified it to be a function I could use in my program.

All atempts of optimizing input.py can go in inputV2.py, see inputV2.py for more info.

"""




def GetKeys():
    import asyncio
    from prompt_toolkit.input import create_input
    from prompt_toolkit.keys import Keys

    global __input_key_ret__ # define a variable in this scope to set the return key to
    __input_key_ret__=None # make it None
    
    async def main() -> None:
        done = asyncio.Event()
        input = create_input()

        def keys_ready():
            for key_press in input.read_keys(): # read key
                # print(key_press)
                
                global __input_key_ret__ # import global return var
                # set return var to keypress
                __input_key_ret__=key_press.key[0:]
                    # from key_press, we get key.
                    # if d was pressed, key looks like 'd'. this with [0:] returns 'd'
                    # but if control-d was pressed, key looks like <Keys.ControlD: 'c-d'>
                    # and we only want 'c-d'. So we use [0:] to get the string out of its Keys.ControlD shell.
                done.set()

        with input.raw_mode():
            with input.attach(keys_ready):
                await done.wait()
        # return ret
    
    asyncio.run(main())
    return __input_key_ret__
