import os
import matplotlib.pyplot as plt
from fuzzy_package.fuzzy_simulation import setup_fuzzy_system

def run_simulation():
    simulator, intensity = setup_fuzzy_system()

    # Inputs for simulation
    simulator.input["frequency"] = 6
    simulator.input["available_time"] = 28
    simulator.input["excess_weight"] = 26
    simulator.input["adherence"] = 7
    simulator.input["fitness"] = 59

    # Run simulation
    simulator.compute()
    output_value = simulator.output["intensity"]
    print(f"Intensity output: {output_value}")
    intensity.view(sim=simulator)

    save_plot(intensity)

def save_plot(intensity):
    base_filename = "intensity_plot"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    counter = 1
    while True:
        filename = os.path.join(output_folder, f"{base_filename}{counter}.png")
        if not os.path.exists(filename):
            plt.savefig(filename)
            print(f"Plot saved as {filename}")
            break
        counter += 1

if __name__ == "__main__":
    run_simulation()
