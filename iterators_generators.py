import random

# Countdown Iterator Class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current

# Fibonacci Generator Function
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Random Number Generator Function
def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)

def main():
    try:
        # Demonstrating Countdown Iterator
        print("Countdown from 5:")
        for number in Countdown(5):
            print(number)

        # Demonstrating Fibonacci Generator
        print("\nFibonacci sequence up to 21:")
        for number in fibonacci_generator(21):
            print(number)

        # Demonstrating Random Number Generator
        print("\n5 Random numbers between 10 and 50:")
        for number in random_number_generator(10, 50, 5):
            print(number)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()