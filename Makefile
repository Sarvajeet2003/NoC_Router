# Makefile for NoC Simulator

# Define Python interpreter
PYTHON = python3

# Define source files
SRC_FILES = main.py FileParser.py Router.py SimulationEngine.py Logger.py \
            SwitchAllocator.py TrafficGenerator.py Crossbar.py InputBuffer.py

# Define input data files
TRAFFIC_FILE = traffic.txt
DELAYS_FILE = delays.txt

# Default target
all: run

# Run the simulation
run:
	$(PYTHON) main.py $(TRAFFIC_FILE) $(DELAYS_FILE)

# Clean up generated files and pycache
clean:
	rm -f *.log
	rm -f __pycache__/*.pyc
	rm -f __pycache__/*/__init__.pyc

# Clean up all generated files, including logs
cleanall: clean
	rm -f *.txt

.PHONY: all run clean cleanall
