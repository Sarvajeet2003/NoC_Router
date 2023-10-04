# InputBuffer.py

class InputBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def push(self, flit):
        if not self.is_full():
            self.buffer.append(flit)
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            return self.buffer.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.buffer[0]
        else:
            return None

    def clear(self):
        self.buffer = []

# Example usage:
# Create an input buffer with a capacity of 5
buffer = InputBuffer(5)

# Push a flit into the buffer
buffer.push("Flit 1")

# Check if the buffer is empty or full
print("Is empty:", buffer.is_empty())  # Should print False
print("Is full:", buffer.is_full())    # Should print False

# Pop a flit from the buffer
popped_flit = buffer.pop()
print("Popped flit:", popped_flit)      # Should print "Flit 1"
