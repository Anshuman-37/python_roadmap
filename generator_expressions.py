# generator = (expression for item in iterable if condition)

# Example 1 generating a squares using a generator expression
squares = (x**2 for x in range(10))

print(squares) # Output: <generator object <genexpr> at 0x...>

for num in squares:
    print(num)
# Outputs numbers from 0 to 81
