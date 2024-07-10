# intensity_control.py
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import numpy as np
import os

def setup_intensity_control():
    # Inputs:
    frequency = ctrl.Antecedent(np.arange(0, 8, 1), "frequency")
    available_time = ctrl.Antecedent(np.arange(20, 91, 1), "available_time")
    excess_weight = ctrl.Antecedent(np.arange(0, 41, 1), "excess_weight")
    adherence = ctrl.Antecedent(np.arange(0, 8, 1), "adherence")
    fitness = ctrl.Antecedent(np.arange(16, 81, 1), "fitness")

    # Output:
    intensity = ctrl.Consequent(np.arange(30, 91, 1), "intensity")

    # Fuzzification
    frequency["low"] = fuzz.trapmf(frequency.universe, [0, 0, 2, 4])
    frequency["moderate"] = fuzz.trimf(frequency.universe, [2, 4, 6])
    frequency["high"] = fuzz.trapmf(frequency.universe, [4, 6, 7, 7])
    available_time["low"] = fuzz.trimf(available_time.universe, [20, 20, 40])
    available_time["medium"] = fuzz.trimf(available_time.universe, [30, 40, 50])
    available_time["high"] = fuzz.trapmf(available_time.universe, [40, 60, 90, 90])
    excess_weight["low"] = fuzz.trimf(excess_weight.universe, [0, 0, 15])
    excess_weight["moderate"] = fuzz.trimf(excess_weight.universe, [5, 15, 30])
    excess_weight["high"] = fuzz.trapmf(excess_weight.universe, [15, 30, 40, 40])
    adherence["low"] = fuzz.trimf(adherence.universe, [0, 0, 3.5])
    adherence["moderate"] = fuzz.trimf(adherence.universe, [0, 3.5, 7])
    adherence["high"] = fuzz.trimf(adherence.universe, [3.5, 7, 7])
    fitness["low"] = fuzz.trapmf(fitness.universe, [16, 16, 20.5, 29.5])
    fitness["low_medium"] = fuzz.trimf(fitness.universe, [20.5, 29.5, 38.5])
    fitness["medium"] = fuzz.trimf(fitness.universe, [29.5, 38.5, 47.5])
    fitness["medium_high"] = fuzz.trapmf(fitness.universe, [38.5, 47.5, 56.5, 56.5])
    fitness["high"] = fuzz.trapmf(fitness.universe, [47.5, 56.5, 80, 80])

    # Output
    intensity["low"] = fuzz.trapmf(intensity.universe, [30, 30, 37.5, 47.5])
    intensity["low_medium"] = fuzz.trimf(intensity.universe, [37.5, 47.5, 62.5])
    intensity["medium"] = fuzz.trimf(intensity.universe, [47.5, 62.5, 72.5])
    intensity["medium_high"] = fuzz.trimf(intensity.universe, [62.5, 72.5, 85])
    intensity["high"] = fuzz.trapmf(intensity.universe, [72.5, 85, 90, 90])

    # Inference
    rule1 = ctrl.Rule(fitness["high"], intensity["high"])
    rule2 = ctrl.Rule(fitness["medium_high"], intensity["medium_high"])
    rule3 = ctrl.Rule(fitness["medium"], intensity["medium"])
    rule4 = ctrl.Rule(fitness["low_medium"], intensity["low_medium"])
    rule5 = ctrl.Rule(fitness["low"], intensity["low"])
    rule6 = ctrl.Rule(available_time["high"] & fitness["high"], intensity["medium_high"])
    rule7 = ctrl.Rule(available_time["high"] & fitness["medium_high"], intensity["medium"])
    rule8 = ctrl.Rule(available_time["high"] & fitness["medium"], intensity["low_medium"])
    rule9 = ctrl.Rule(frequency["low"] & fitness["high"], intensity["high"])
    rule10 = ctrl.Rule(frequency["low"] & fitness["medium_high"], intensity["high"])
    rule11 = ctrl.Rule(frequency["low"] & fitness["medium"], intensity["medium_high"])
    rule12 = ctrl.Rule(frequency["low"] & fitness["low_medium"], intensity["medium"])
    rule13 = ctrl.Rule(frequency["low"] & fitness["low"], intensity["low_medium"])
    rule14 = ctrl.Rule(available_time["low"] & fitness["high"], intensity["high"])
    rule15 = ctrl.Rule(available_time["low"] & fitness["medium_high"], intensity["high"])
    rule16 = ctrl.Rule(available_time["low"] & fitness["medium"], intensity["medium_high"])
    rule17 = ctrl.Rule(available_time["low"] & fitness["low_medium"], intensity["medium"])
    rule18 = ctrl.Rule(available_time["low"] & fitness["low"], intensity["low_medium"])
    rule19 = ctrl.Rule(frequency["high"] & fitness["high"], intensity["medium_high"])
    rule20 = ctrl.Rule(frequency["high"] & fitness["medium_high"], intensity["medium"])
    rule21 = ctrl.Rule(frequency["high"] & fitness["medium"], intensity["low_medium"])
    rule22 = ctrl.Rule(frequency["high"] & fitness["low_medium"], intensity["low"])
    rule23 = ctrl.Rule(adherence["high"] & fitness["high"], intensity["high"])
    rule24 = ctrl.Rule(adherence["high"] & fitness["medium_high"], intensity["high"])
    rule25 = ctrl.Rule(adherence["high"] & fitness["medium"], intensity["medium_high"])
    rule26 = ctrl.Rule(adherence["high"] & fitness["low_medium"], intensity["medium"])
    rule27 = ctrl.Rule(adherence["high"] & fitness["low"], intensity["low_medium"])
    rule28 = ctrl.Rule(adherence["low"] & fitness["high"], intensity["medium_high"])
    rule29 = ctrl.Rule(adherence["low"] & fitness["medium_high"], intensity["medium"])
    rule30 = ctrl.Rule(adherence["low"] & fitness["medium"], intensity["low_medium"])
    rule31 = ctrl.Rule(adherence["low"] & fitness["low_medium"], intensity["low"])
    rule32 = ctrl.Rule(adherence["moderate"] & fitness["high"], intensity["high"])
    rule33 = ctrl.Rule(adherence["moderate"] & fitness["medium_high"], intensity["medium_high"])
    rule34 = ctrl.Rule(adherence["moderate"] & fitness["medium"], intensity["medium"])
    rule35 = ctrl.Rule(adherence["moderate"] & fitness["low_medium"], intensity["low_medium"])
    rule36 = ctrl.Rule(adherence["moderate"] & fitness["low"], intensity["low"])
    rule37 = ctrl.Rule(excess_weight["moderate"] & fitness["low"], intensity["low_medium"])
    rule38 = ctrl.Rule(excess_weight["moderate"] & fitness["low_medium"], intensity["medium"])
    rule39 = ctrl.Rule(excess_weight["moderate"] & fitness["medium"], intensity["medium_high"])
    rule40 = ctrl.Rule(excess_weight["moderate"] & fitness["medium_high"], intensity["high"])

    intensity_ctrl = ctrl.ControlSystem(
        [
            rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
            rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
            rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28,
            rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37,
            rule38, rule39, rule40,
        ]
    )
    intensity_simulator = ctrl.ControlSystemSimulation(intensity_ctrl)

    return intensity_simulator, intensity

def run_intensity_simulation():
    intensity_simulator, intensity = setup_intensity_control()

    # Simulation
    intensity_simulator.input["frequency"] = 6  # 0 - 7
    intensity_simulator.input["available_time"] = 28  # 20 - 90
    intensity_simulator.input["excess_weight"] = 26  # 0 - 40
    intensity_simulator.input["adherence"] = 7  # 0 - 8
    intensity_simulator.input["fitness"] = 59  # 16 - 80

    # Defuzzification
    intensity_simulator.compute()
    print(intensity_simulator.output["intensity"])
    output_value = intensity_simulator.output["intensity"]
    intensity.view(sim=intensity_simulator)

    base_filename = "intensity_plot"
    output_folder = "output"
    counter = 1

    os.makedirs(output_folder, exist_ok=True)

    while True:
        filename = os.path.join(output_folder, f"{base_filename}{counter}.png")
        if not os.path.exists(filename):
            break
        counter += 1

    plt.savefig(filename)

if __name__ == "__main__":
    run_intensity_simulation()
