from itertools import product 
variables = ['p', 'q']

combinations = list(product([1, 0], repeat=len(variables)))
def logic_expression(p, q):
    return (p == q) 

print("----------------------------------------------------------------------")
print('\t\t\t\t'.join(variables + ['p<=>q']))
print("----------------------------------------------------------------------")

for combo in combinations:
    values = list(combo)
    result = int(logic_expression(*values))

    print('\t\t\t\t'.join([str(value) for value in values + [result]]))
    print("----------------------------------------------------------------------")