"""
This file is a failed attempt at simplyfieing input.py.
DO NOT USE!!!!!!
This function is broken, idk why. All attempts at optimizing/simplifying input.py go here.
"""

def attempt1(): # does not work
    from prompt_toolkit.input import create_input
    from prompt_toolkit.keys import Keys
    input = create_input()
    
    with input.raw_mode():
        data=input.read_keys()[0].data
        return data