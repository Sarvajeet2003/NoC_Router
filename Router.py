from InputBuffer import InputBuffer
from SwitchAllocator import SwitchAllocator
from Crossbar import Crossbar

class Router:
    def __init__(self, router_id,buffer_delay,sa_delay,xbar_delay):
        self.router_id = router_id
        self.input_buffer = InputBuffer(buffer_delay)
        self.crossbar = Crossbar(xbar_delay)
        self.switch_allocator = SwitchAllocator(sa_delay)

    def isempty(self):
        if((self.input_buffer.value == None) and (self.crossbar.value == None) and (self.switch_allocator.value == None)):
            return True
        return False

    def __str__(self):
        s = ""
        s += f"Router ID : {self.router_id} \n"
        if(not self.input_buffer.isempty()):
            s += f"Input Buffer Value : {self.input_buffer.value[2]} \n "
        if(self.input_buffer.isempty()):
            s += f"Input Buffer Value : None \n"
        if(not self.switch_allocator.isempty()):
            s += f"Switch Allocator Value : {self.switch_allocator.value[2]} \n "
        if(self.switch_allocator.isempty()):
            s += f"Switch Allocator Value : None \n "
        if(not self.crossbar.isempty()):
            s += f"CrossBar Value : {self.crossbar.value[2]} \n"
        if(self.crossbar.isempty()):
            s += f"CrossBar Value : None \n"

        return s


    def inject(self,flit_details):
        self.input_buffer.value = flit_details

    def getflit(self): #returns flit details
        if(not self.crossbar.isempty()):
            return self.crossbar.value
        if(not self.switch_allocator.isempty()):
            return self.switch_allocator.value
        if(not self.input_buffer.isempty()):
            return self.input_buffer.value

    def update1(self,nextrouter):
        if(not self.crossbar.isempty()):
            nextrouter.input_buffer.value = self.crossbar.value
        if(not self.switch_allocator.isempty()):
            self.crossbar.value = self.switch_allocator.value
        if(not self.input_buffer.isempty()):
            self.switch_allocator.value = self.input_buffer.value

        self.input_buffer.value = None

    def update(self,next_id,allrouter):
        nextrouter = allrouter[next_id]
        nextrouter.input_buffer.value = self.crossbar.value
        self.crossbar.value = self.switch_allocator.value
        self.switch_allocator.value = self.input_buffer.value
        self.input_buffer.value = None