import pytest
from fuzzy_package.fuzzy_simulation import setup_fuzzy_system

@pytest.fixture
def intensity_simulator():
    simulator, _ = setup_fuzzy_system()
    return simulator

def test_intensity_output(intensity_simulator):
    intensity_simulator.input["frequency"] = 6
    intensity_simulator.input["available_time"] = 28
    intensity_simulator.input["excess_weight"] = 26
    intensity_simulator.input["adherence"] = 7
    intensity_simulator.input["fitness"] = 59
    
    intensity_simulator.compute()

    assert intensity_simulator.output["intensity"] is not None
    assert intensity_simulator.output["intensity"] == 78.53164774681801
