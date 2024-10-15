# The yield keyword in Python is used to create generator functions.
# A generator function is a special type of function that returns a generator iterator, which can be used
# to produce a sequence of values over time. Instead of computing and returning all the values at once,
# a generator yields one value at a time, suspending its state between each yield and resuming from where it
# left off when the next value is requested.

# Example 1
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)

for num in counter:
    print(num)
# Output: 1 2 3 4 5

# Example 2
# Creating a generator that yields an infinite sequence of Fibonacci numbers:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))
# Output: 0 1 1 2 3 5 8 13 21 34
