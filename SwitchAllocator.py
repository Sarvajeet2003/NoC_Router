# SwitchAllocator.py

class SwitchAllocator:
    def __init__(self,delay):
        self.delay = delay
        self.value = None
        self.input_port = None
        self.output_port = None

    def allocate_flit(self, router_id, next_router_id, flit):
        source_x, source_y = router_id % 3, router_id // 3
        dest_x, dest_y = next_router_id % 3, next_router_id // 3

        if source_x < dest_x:
            output_port = self.output_ports['East']
        elif source_x > dest_x:
            output_port = self.output_ports['West']
        elif source_y < dest_y:
            output_port = self.output_ports['North']
        else:
            output_port = self.output_ports['South']

        
