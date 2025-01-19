unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}
def extract_parameter(unit_name, parameter_name, index): #create function and define 
    if unit_name not in unit_operations_data:
        return "Invalid input"  # Check if unit_name exists in the dictionary
    if parameter_name not in unit_operations_data[unit_name]:
        return "Invalid input"  # Check if parameter_name exists in the unit's data
    parameter_values = unit_operations_data[unit_name][parameter_name] # Try to retrieve the list of parameter values
    if index < 0 or index >= len(parameter_values):
        return "Invalid input"  # Check if the index is out of range
    value = parameter_values[index] # Retrieve the value based on the given index
    return f"{unit_name}_{parameter_name}_{value}" # Return the formatted string
