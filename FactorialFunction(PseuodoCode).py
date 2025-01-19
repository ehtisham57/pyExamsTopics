#For function Factorial

def calculate_fac(n):
    if n < 0:
        return
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# INPUTS
number = int(input("Enter a number to find its factorial: "))
result = calculate_fac(number)
print(f"The factorial of {number} is: {result}")