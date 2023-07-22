"""
This file should translate note names to filenames based on a dictionary
made by the user. It is imported by interpreter.py.

It also handles converting musical waiting notation to seconds for the wait command.





"""


class map:
    mappings=dict()
    def map(self,key,layer,sample):
        mapping=f"{layer}\t{sample}".encode() # compose a result and encode it
        self.mappings[key]=mapping
    
    def getmap(self,key):
        try:
            preret=self.mappings[key].decode() # get mapping and decode it
        except KeyError:
            ret=[None,None]
            return ret
        ret=preret.split("\t") # split it on seperator
        return ret