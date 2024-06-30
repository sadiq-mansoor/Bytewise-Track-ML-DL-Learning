def sqrt(a):
    try:
        if a < 0:
            raise ValueError("Error: Cannot take the square root of a negative number.")
        return a ** 0.5
    except TypeError:
        print("Error: Invalid input. Please provide a number.")