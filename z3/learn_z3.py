from z3 import *

x = Int('x')
y = Real('y')
print ((x + 1).sort())
print ((y + 1).sort())
print ((x >= 2).sort())