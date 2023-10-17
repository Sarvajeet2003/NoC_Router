# Network on Chip (NoC) Simulator

## Project Description
The provided Python code is a simulation of a Network-on-Chip (NOC) using a simple router-based model. It simulates the flow of packets (flits) between routers and tracks the time it takes for these packets to traverse the NOC. The code is also designed to validate the input traffic data and ensure that it adheres to specific rules and constraints.

## Components

## Router Class: 
The code defines a Router class that represents a router in the NOC. Each router has input buffers, a switch allocator, and a crossbar for handling incoming flits. Routers can inject, receive, and transfer flits to other routers.

## Algorithm Used: 
The code uses a function called xy1 to calculate the next router to which a flit should be sent based on the current router's location and the destination router's location. This function calculates the XY-routing path.

## Traffic Simulation: 
The main simulation logic handles the flow of flits through the NOC. It processes traffic data provided in the traffic.txt file and tracks the time taken by each flit to traverse the NOC. The simulation considers input buffer delays, switch allocator delays, and crossbar delays.

## Error Handling: 
The code includes error checks to ensure that the input traffic data and delay data are correctly formatted and adhere to specified rules. It checks for valid router IDs, flit types, and ensures that source and destination routers are not the same. It also checks for matching last two digits in the provided data.

## PDF Report Generation: 
The code generates a PDF report (report.pdf) that includes details about the simulation. It provides information about the time taken by head, body, and tail flits of each packet, their source, destination and also the element of the destination router at which the flit is arriving. In addition to this, it also showcases the total time taken by every flit to leave the NoC, the clock cycles used, and the clock frequency.

## Log File: 
The code redirects standard output to a log file named Log_File.txt, which captures the simulation's progress and router states at each clock cycle.

## Usage Instructions
To use the code, follow these steps:

Input Data: Ensure you have the following input files in the same directory as the code:
## traffic.txt: 
Contains traffic data specifying the clock cycle, source, destination, and flit details for each packet.
## delays.txt: 
Contains delay values for the input buffer, switch allocator, and crossbar.

# Run the Code: 
Execute the code. It will simulate the NOC and generate the output files.

## Output Files:

# Log_File.txt: 
Captures the simulation progress and router states at each clock cycle.
# report.pdf: 
Contains a detailed report on the simulation, including flit time information and the destination router for each flit being injected.
