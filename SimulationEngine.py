import time

class SimulationEngine:
    def __init__(self, routers, routing_algorithm, crossbar):
        self.routers = routers
        self.routing_algorithm = routing_algorithm
        self.crossbar = crossbar
        self.current_cycle = 0

    def run_simulation(self, traffic_data):
        """Run the NoC simulation based on traffic data."""
        print("Starting NoC simulation...")
        total_cycles = max(packet[0] for packet in traffic_data) + 1  # Determine total simulation cycles
        for cycle in range(total_cycles):
            self.current_cycle = cycle
            self.process_traffic(traffic_data)
            time.sleep(0.1)  # Simulate clock cycles with a fixed delay (adjust as needed)

        print("NoC simulation completed.")

    def process_traffic(self, traffic_data):
        """Process incoming traffic for the current cycle."""
        for packet in traffic_data:
            if packet[0] == self.current_cycle:
                source_router_id, destination_router_id, flit_type = packet[1], packet[2], packet[3]
                source_router = self.routers[source_router_id]
                destination_router = self.routers[destination_router_id]

                # Create and inject the flit into the source router
                flit = Flit(flit_type, destination_router_id)
                source_router.inject_flit(flit)

    def get_current_cycle(self):
        """Get the current cycle number in the simulation."""
        return self.current_cycle

class Flit:
    def __init__(self, flit_type, destination_router_id):
        self.flit_type = flit_type
        self.destination_router_id = destination_router_id
