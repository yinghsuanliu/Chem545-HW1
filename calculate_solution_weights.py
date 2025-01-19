molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

solutions_needed = ['NaCl-0.3M', 'H2SO4-0.6M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']
def calculate_solution_weights(molecular_weights, solutions_needed):
    result = []
    for solution in solutions_needed:
        if '-' in solution and solution.endswith('M'):
            chemical, concentration = solution.rsplit('-', 1) # Check if the format is valid and split the chemical and concentration
            if chemical in molecular_weights and concentration[:-1].replace('.', '', 1).isdigit():
                concentration = float(concentration[:-1])  # Remove 'M' and convert to float
                weight = molecular_weights[chemical] * concentration
                result.append(f"{chemical}-{concentration}M-{weight:.2f}g")
            else:
                result.append("unknown")
        else:
            result.append("unknown")
    return result

output = calculate_solution_weights(molecular_weights, solutions_needed)
print(output)
