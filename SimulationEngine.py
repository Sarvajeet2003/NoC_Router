# SimulationEngine.py

import time

class SimulationEngine:
    def __init__(self, routers, delay):
        self.routers = routers
        self.delay = delay
        self.current_cycle = 0

    def run_simulation(self, total_cycles):
        """Run the NoC simulation for a specified number of cycles."""
        print("Starting NoC simulation...")
        for cycle in range(total_cycles):
            self.current_cycle = cycle
            self.process_routers()
            time.sleep(self.delay)  # Simulate clock cycles by sleeping

        print("NoC simulation completed.")

    def process_routers(self):
        """Process all routers in the NoC for the current cycle."""
        for router in self.routers:
            router.process_flits()

    def get_current_cycle(self):
        """Get the current cycle number in the simulation."""
        return self.current_cycle
