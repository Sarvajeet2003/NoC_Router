# SwitchAllocator.py

class SwitchAllocator:
    def __init__(self, input_ports, output_ports):
        self.input_ports = input_ports
        self.output_ports = output_ports

    def allocate_flit(self, router_id, next_router_id, flit):
        """Allocate a flit to the appropriate output port based on XY routing."""
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

        # Forward the flit to the selected output port
        output_port.receive_flit(flit)
