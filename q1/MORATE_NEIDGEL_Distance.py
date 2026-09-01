import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate using the Euclidean distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the answer rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")

"""
Reflection: Using the functions from the math library helped a lot when typing this code, as it saves time, makes coding easier, and reduces the chances of having bugs. The math.pow() squares values, while math.sqrt() helps. Using the "input math", it helps with activating extra tools involving math, using "math." to access them. Converting inputs to floats ensures the program uses decimal entries. 
"""
