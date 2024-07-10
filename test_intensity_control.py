import sys
import os
import pytest

# Add the project root directory to the sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from intensity_control import setup_intensity_control

@pytest.fixture
def intensity_simulator():
    simulator, _ = setup_intensity_control()
    return simulator

def test_intensity_output(intensity_simulator):
    intensity_simulator.input["frequency"] = 6
    intensity_simulator.input["available_time"] = 28
    intensity_simulator.input["excess_weight"] = 26
    intensity_simulator.input["adherence"] = 7
    intensity_simulator.input["fitness"] = 59
    intensity_simulator.compute()
    assert intensity_simulator.output["intensity"] is not None


