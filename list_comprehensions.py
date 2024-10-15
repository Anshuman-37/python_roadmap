## new_list = [expression for item in iterable if condition]

# Example 1
numbers = [i for i in range(10)]

# Example 2
squares = [i**2 for i in range(10)]

# Example 3 if checks
even_numbers = [i for i in range(10) if i % 2 == 0]

# Example 4 double loops
coordinates = [(x, y) for x in range(3) for y in range(2)]

# Example 5 Complex Logic
nums = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]

# Example 6 Flattening a list
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]

