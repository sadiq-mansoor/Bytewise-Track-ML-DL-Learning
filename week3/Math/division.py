def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return a / b
    except TypeError:
        print("Error: Invalid input. Please provide numbers.")