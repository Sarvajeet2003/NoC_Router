# TrafficGenerator.py

import random

class TrafficGenerator:
    def __init__(self, routers, traffic_file):
        self.routers = routers
        self.traffic_file = traffic_file
        self.current_cycle = 0

    def generate_traffic(self):
        """Generate and inject traffic into the NoC based on the traffic file."""
        try:
            with open(self.traffic_file, 'r') as file:
                for line in file:
                    cycle, source, destination, flit_type = map(int, line.strip().split())

                    if cycle == self.current_cycle:
                        source_router = self.routers[source]
                        destination_router = self.routers[destination]

                        # Create a packet with header, body, and tail flits
                        packet = [flit_type] * 3

                        # Inject the packet into the source router
                        source_router.input_ports['Local'].receive_packet(packet, destination_router)

                    self.current_cycle += 1

            print("Traffic generation completed.")

        except FileNotFoundError:
            print(f"Error: Traffic file '{self.traffic_file}' not found.")

        except Exception as e:
            print("Error:", str(e))
