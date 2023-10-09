# InputBuffer.py

class InputBuffer:
    def __init__(self,delay):
        self.delay = delay
        self.value = None
'''
    def is_empty(self):
        return (self.value == None)


    def push(self, flit):
        if self.value == None:
            self.value = flit
            return True
        else:
            return False

    def pop(self):
        if self.value != None:
            val = self.value
            self.value = None
            return val
        else:
            return None

    def peek(self):
        if self.value != None:
            return self.value
        else:
            return None

    def clear(self):
        self.value = None

if(__name__ == '__main__'):
    buffer = InputBuffer(5)

    # Push a flit into the buffer
    buffer.push("Flit 1")

    # Check if the buffer is empty or full
    print("Is empty:", buffer.is_empty())  # Should print False
    print("Is full:", buffer.is_full())    # Should print False

    # Pop a flit from the buffer
    popped_flit = buffer.pop()
    print("Popped flit:", popped_flit)      # Should print "Flit 1"'''
