# Intensity Control with Fuzzy Logic

This Python script demonstrates a simplified intensity control system using fuzzy logic. The script utilizes the scikit-fuzzy library to define fuzzy variables, rules, and perform inference to determine the intensity based on input variables.

## Installation

Before running the script, make sure to install the required libraries. It's recommended to create a virtual environment to manage these libraries separately. Here's how to set up the environment:
Python 3.12 was used in this project

1. **Create a Virtual Environment (Optional)**

   You can create a virtual environment using Python's built-in `venv` module. If you're not familiar with `venv`, you can refer to the [official Python documentation](https://docs.python.org/3/library/venv.html) for more information on how to create and manage virtual environments.

2. **Install Required Libraries**

```
pip install -r requirements.txt
```

## Usage

To observe different outcomes of the intensity control, you can adjust the input variables: `frequency`, `available_time`, `excess_weight`, `adherence`, and `fitness`. These variables represent different factors influencing the intensity. Modify their values as needed to see how the fuzzy logic system calculates the intensity output.

```python
intensity_simulator.input["frequency"] = 6
intensity_simulator.input["available_time"] = 28
intensity_simulator.input["excess_weight"] = 26
intensity_simulator.input["adherence"] = 7
intensity_simulator.input["fitness"] = 59
```

## Running the Script

Execute the Python script to perform the intensity control modeling and view the output. The script will also save the resulting intensity plot in the "output" folder with a unique filename to prevent overwriting previous results.

```
python main.py
```

## Tests
Tests can be run by the following command: 

```
pytest
```

## Reference

This code is based on the research paper:

- [Fuzzy Logic-Based Intensity Control in Physical Activities for Health Promotion](https://www.reciis.icict.fiocruz.br/index.php/reciis/article/view/941)

Please refer to the paper for a detailed explanation of the fuzzy logic model and its application.
