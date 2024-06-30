def subtract(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Invalid input. Please provide numbers.")