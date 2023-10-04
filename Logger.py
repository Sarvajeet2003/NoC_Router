# Logger.py

class Logger:
    def __init__(self):
        self.log_entries = []

    def log_event(self, cycle, router_id, element, flit):
        """Log an event in the simulation."""
        log_entry = f"Cycle {cycle}: Router {router_id}, Element {element}, Flit {flit}"
        self.log_entries.append(log_entry)

    def generate_log_file(self, simulation_engine):
        """Generate the log file based on simulation events."""
        if not self.log_entries:
            return  # Nothing to log

        file_name = "simulation_log.txt"

        try:
            with open(file_name, "w") as log_file:
                for log_entry in self.log_entries:
                    log_file.write(log_entry + "\n")

            print(f"Log file '{file_name}' generated successfully.")

        except Exception as e:
            print("Error: Unable to generate log file.", str(e))
