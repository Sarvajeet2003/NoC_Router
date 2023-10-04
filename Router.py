class Router:
    def __init__(self, router_id, delay=0):
        self.router_id = router_id
        self.delay = delay
        self.input_buffer = []  # List to store incoming flits
        self.routing_algorithm = None
        self.crossbar = None
        self.switch_allocator = None

    def inject_packet(self, packet, destination_router):
        """Inject a packet into the router."""
        # Assuming packets are injected into the local input port
        self.input_ports['Local'].receive_packet(packet, destination_router)

    def inject_flit(self, flit):
        """Inject a flit into the router's input buffer."""
        self.input_buffer.append(flit)

    def set_switch_allocator(self, switch_allocator):
        """Set the switch allocator for the router."""
        self.switch_allocator = switch_allocator

    def receive_flit(self, flit):
        """Simulate processing the received flit."""
        print(f"Router {self.router_id} received flit: {flit}")

    def process_flits(self):
        """Process flits in the router."""
        if not self.input_buffer:
            return  # No flits to process

        # Process header flits
        header_flit = self.input_buffer[0]
        flit_type = header_flit[0]

        if flit_type == 0:  # Header flit
            source, destination, _ = header_flit[1], header_flit[2], header_flit[3]

            # Implement routing logic based on routing algorithm (XY or YX)
            if self.routing_algorithm == "XY":
                if self.router_id % 3 == destination % 3:  # Check X-coordinate
                    next_router_id = destination
                else:
                    next_router_id = self.router_id + 3 if destination > self.router_id else self.router_id - 3
            elif self.routing_algorithm == "YX":
                if self.router_id // 3 == destination // 3:  # Check Y-coordinate
                    next_router_id = destination
                else:
                    next_router_id = self.router_id + 1 if destination > self.router_id else self.router_id - 1

            # Pass the flit to the next router through the crossbar and switch allocator
            self.crossbar.route_flit(self.router_id, next_router_id, header_flit)
            self.switch_allocator.allocate_flit(self.router_id, next_router_id, header_flit)

        # Remove processed flits from the input buffer
        self.input_buffer.pop(0)

    def set_routing_algorithm(self, routing_algorithm):
        """Set the routing algorithm for the router."""
        self.routing_algorithm = routing_algorithm