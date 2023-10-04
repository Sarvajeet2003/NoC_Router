# Crossbar.py

class Crossbar:
    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.input_ports = [[] for _ in range(num_inputs)]
        self.output_ports = [[] for _ in range(num_outputs)]

    def connect(self, input_port, output_port):
        """Connect an input port to an output port."""
        self.input_ports[input_port].append(output_port)
        self.output_ports[output_port].append(input_port)

    def route(self):
        """Route flits through the crossbar."""
        for input_port in range(self.num_inputs):
            if self.input_ports[input_port]:
                flit = self.input_ports[input_port].pop(0)  # Get the next flit in the input
                output_port = self.output_ports[flit].pop(0)  # Get the output port for the flit
                # Send the flit to the output port (simulate routing)
                self.input_ports[output_port].append(flit)

# Example usage of the Crossbar class:
# crossbar = Crossbar(num_inputs, num_outputs)
# crossbar.connect(input_port, output_port)
# crossbar.route()
