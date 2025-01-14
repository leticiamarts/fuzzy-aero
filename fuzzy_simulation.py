from skfuzzy import control as ctrl
from fuzzy_variables import create_fuzzy_variables
from fuzzy_rules import create_fuzzy_rules

def setup_fuzzy_system():
    frequency, available_time, excess_weight, adherence, fitness, intensity = create_fuzzy_variables()
    rules = create_fuzzy_rules(frequency, available_time, excess_weight, adherence, fitness, intensity)
    control_system = ctrl.ControlSystem(rules)
    simulator = ctrl.ControlSystemSimulation(control_system)
    return simulator, intensity
