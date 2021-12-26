import math

x = 10
y = 4

print(f'{x} + {y} = ', x + y)
print(f'{x} - {y} = ', x - y)
print(f'{x} X {y} = ', x * y)
print(f'{x} / {y} = ', x / y)
print(f'{x} % {y} = ', x % y)
print(f'{x} ^ {y} = ', x ** y)

# Precedence
print(10 / (5 - 3) * 2 ** 2 + 7)

# functions / math-modules
x = 2.5
print(f'Floor of {x}:', math.floor(x))
print(f'Ceiling of {x}:', math.ceil(x))
