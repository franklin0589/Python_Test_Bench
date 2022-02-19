import numpy
import theano.tensor as tt
from theano import function

# Adding two Numbers
# x = tt.dscalar('x')
# y = tt.dscalar('y')
# z = x+y
# f = function([x, y], z)

#Adding two Matrices
# x = tt.dmatrix('x')
# y = tt.dmatrix('y')
# z = x + y
# f = function([x, y], z)
# print(f([[1, 2], [3, 4]], [[10, 20], [30, 40]]))


# a = tt.vector()
# b = tt.vector()
# out = a**2  +b**2 + 2*a*b
# f = function([a,b],out)
# print(f([0,1,2],[0,1,2]))

# x = tt.dmatrix('x')
# s = 1 / (1 + tt.exp(-x))
# logistic = function([x], s)
# print(logistic([[0, 1], [-1, -2]]))

a, b = tt.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff**2
f = function([a, b], [diff, abs_diff, diff_squared])
print(f([[1, 1], [1, 1]], [[0, 1], [2, 3]]))