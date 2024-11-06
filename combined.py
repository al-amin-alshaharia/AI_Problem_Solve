from itertools import product

def evaluate_proposition(variables, proposition):
    truth_values = []
    for assignment in product([False, True], repeat=len(variables)):
        assignment_dict = dict(zip(variables, assignment))
        result = eval(proposition, assignment_dict)
        truth_values.append((assignment_dict, result))
    return truth_values

def print_truth_table(variables, proposition, proposition_name):
    truth_values = evaluate_proposition(variables, proposition)

    # Print header
    header = list(variables) + [proposition_name]
    print(" | ".join(header))

    # Print separator
    separator = "+".join(["-" * (len(v) + 2) for v in header])
    print(separator)

    # Print truth values
    for assignment, result in truth_values:
        values = [str(assignment[var]) for var in variables] + [str(result)]
        print(" | ".join(values))

# Propositions
prop_a = "(raining_outside == cloudy_day)"
prop_b = "(final_exam_score == 100 and not grade_in_class == 'A')"
prop_c = "(take_advil or take_tylenol)"
prop_d = "(studied_hard or extremely_bright)"
prop_e = "(rock and island)"

# Variables
variables_a = ['raining_outside', 'cloudy_day']
variables_b = ['final_exam_score', 'grade_in_class']
variables_c = ['take_advil', 'take_tylenol']
variables_d = ['studied_hard', 'extremely_bright']
variables_e = ['rock', 'island']

# Print truth tables
print_truth_table(variables_a, prop_a, 'a')
print_truth_table(variables_b, prop_b, 'b')
print_truth_table(variables_c, prop_c, 'c')
print_truth_table(variables_d, prop_d, 'd')
print_truth_table(variables_e, prop_e, 'e')
