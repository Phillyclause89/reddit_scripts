import numpy as np

equation_arr = np.array(np.empty(100), dtype="str")
for i, x in enumerate(np.arange(100)):
    equation = "2*{}={}".format(x, (2 * x))
    equation_arr[i] = equation

print(equation_arr)
