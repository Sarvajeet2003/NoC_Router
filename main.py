import argparse
from FileParser import read_traffic_file, read_delays_file
from Router import Router
from SimulationEngine import SimulationEngine
from Logger import Logger
from SwitchAllocator import SwitchAllocator
from TrafficGenerator import TrafficGenerator
from Crossbar import Crossbar  # Import the Crossbar class

# main.py

NUM_ROWS = 3
NUM_COLS = 3

def main():
    routers = [Router(router_id) for router_id in range(9)]
    input_ports = {'North': None, 'South': None, 'East': None, 'West': None}
    output_ports = {'North': None, 'South': None, 'East': None, 'West': None}
    switch_allocator = SwitchAllocator(input_ports, output_ports)
    traffic_file = "traffic.txt"  # Specify the path to your traffic file
    traffic_generator = TrafficGenerator(routers, traffic_file)
    
    # Create a crossbar for the NoC
    num_inputs = NUM_ROWS * NUM_COLS
    num_outputs = NUM_ROWS * NUM_COLS
    crossbar = Crossbar(num_inputs, num_outputs)
    
    parser = argparse.ArgumentParser(description="Network-on-Chip (NoC) Simulator")
    parser.add_argument("traffic_file", help="Path to the traffic file")
    parser.add_argument("delays_file", help="Path to the delays file")
    parser.add_argument("--routing_algorithm", choices=["XY", "YX"], default="XY", help="Routing algorithm (default: XY)")
    args = parser.parse_args()
    
    for router in routers:
        router.set_switch_allocator(switch_allocator)
    
    # Read and parse input files
    traffic_data = read_traffic_file(args.traffic_file)
    delays_data = read_delays_file(args.delays_file)
    
    if traffic_data is None or delays_data is None:
        return  # Exit if there was an error reading the files
    
    # Create routers and set up the simulation environment
    routers = []
    for router_id, delay in delays_data.items():
        router = Router(router_id, delay)
        routers.append(router)
    
    # Initialize the simulation engine
    simulation_engine = SimulationEngine(routers, args.routing_algorithm, crossbar)  # Pass the crossbar instance
    
    # Start the simulation
    simulation_engine.run_simulation(traffic_data)
    
    # Generate log file
    logger = Logger()
    logger.generate_log_file(simulation_engine)

if __name__ == "__main__":
    main()
