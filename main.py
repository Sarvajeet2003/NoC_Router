import argparse
from FileParser import read_traffic_file, read_delays_file
from Router import Router
from SimulationEngine import SimulationEngine
from Logger import Logger
from SwitchAllocator import SwitchAllocator
from TrafficGenerator import TrafficGenerator
from Crossbar import Crossbar
from InputBuffer import InputBuffer

# main.py

NUM_ROWS = 3
NUM_COLS = 3

def main(traffic_file, delays_file, routing_algorithm):
    # Read and parse input files
    traffic_data = read_traffic_file(traffic_file)
    delays_data = read_delays_file(delays_file)

    if traffic_data is None or delays_data is None:
        return  # Exit if there was an error reading the files

    # Create dictionaries for input and output ports
    input_ports = {'North': None, 'South': None, 'East': None, 'West': None}
    output_ports = {'North': None, 'South': None, 'East': None, 'West': None}

    routers = []
    input_buffers = {}  # Create a dictionary to store input buffers for each router

    # Specify the buffer capacity (you can adjust this value as needed)
    buffer_capacity = 5

    for router_id, delay in delays_data.items():
        router = Router(router_id, delay)
        routers.append(router)

        # Create an input buffer for the router
        input_buffers[router_id] = InputBuffer(buffer_capacity)

    # Create a crossbar for the NoC
    num_inputs = NUM_ROWS * NUM_COLS
    num_outputs = NUM_ROWS * NUM_COLS
    crossbar = Crossbar(num_inputs, num_outputs)

    switch_allocator = SwitchAllocator(input_ports, output_ports)

    for router in routers:
        router.set_switch_allocator(switch_allocator)

    # Create a traffic generator
    traffic_generator = TrafficGenerator(routers, traffic_data)

    # Initialize the simulation engine with the crossbar
    simulation_engine = SimulationEngine(routers, routing_algorithm, crossbar)

    # Start the simulation
    total_cycles = 1000  # Define the total number of simulation cycles
    logger = Logger()
    for cycle in range(total_cycles):
        # Your simulation logic here

        # Replace element and flit with meaningful information
        router_id = 0  # Replace with the appropriate router ID
        element = "Input Buffer"  # Replace with the specific component name
        flit = "Flit 1"  # Replace with the relevant flit or packet
        logger.log_event(cycle, router_id, element, flit)

    # Generate log file
    
    logger.generate_log_file(simulation_engine)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network-on-Chip (NoC) Simulator")
    parser.add_argument("traffic_file", help="Path to the traffic file")
    parser.add_argument("delays_file", help="Path to the delays file")
    parser.add_argument("--routing_algorithm", choices=["XY", "YX"], default="XY", help="Routing algorithm (default: XY)")
    args = parser.parse_args()
    main(args.traffic_file, args.delays_file, args.routing_algorithm)
