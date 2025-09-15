# Create a lambda function
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"

# create a list of tuples
inputs = [(1, 3), (9, 0), (10, 8)]
for x,y in inputs:
    print(f"Inputs: {x}, {y}")
    print(f"Add: {add(x,y)}")
    print(f"Subtract: {subtract(x,y)}")
    print(f"Multiply: {multiply(x,y)}")
    print(f"Divide: {divide(x,y)}")