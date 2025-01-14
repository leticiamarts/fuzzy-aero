from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

def create_fuzzy_variables():
    # Inputs
    frequency = ctrl.Antecedent(np.arange(0, 8, 1), "frequency")
    available_time = ctrl.Antecedent(np.arange(20, 91, 1), "available_time")
    excess_weight = ctrl.Antecedent(np.arange(0, 41, 1), "excess_weight")
    adherence = ctrl.Antecedent(np.arange(0, 8, 1), "adherence")
    fitness = ctrl.Antecedent(np.arange(16, 81, 1), "fitness")

    # Output
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

    intensity["low"] = fuzz.trapmf(intensity.universe, [30, 30, 37.5, 47.5])
    intensity["low_medium"] = fuzz.trimf(intensity.universe, [37.5, 47.5, 62.5])
    intensity["medium"] = fuzz.trimf(intensity.universe, [47.5, 62.5, 72.5])
    intensity["medium_high"] = fuzz.trimf(intensity.universe, [62.5, 72.5, 85])
    intensity["high"] = fuzz.trapmf(intensity.universe, [72.5, 85, 90, 90])

    return frequency, available_time, excess_weight, adherence, fitness, intensity
