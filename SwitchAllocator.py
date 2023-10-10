# SwitchAllocator.py

class SwitchAllocator:
    def __init__(self,delay):
        self.delay = delay
        self.value = None #contain flit_details as list 

    def isempty(self):
        return self.value == None

        
