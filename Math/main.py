import Math as Mat
from Mat.addition import add
from Mat.subtraction import subtract
from Mat.multiplication import multiply
from Mat.division import divide
from Mat.modulus import modulus
from Mat.exponentiation import exponentiate
from Mat.square_root import sqrt

def main():
    try:
        # demonstrates addition
        print("Addition: 5 + 3 =", add(5, 3))
        
        # demonstrates subtraction
        print("Subtraction: 5 - 3 =", subtract(5, 3))
        
        # demonstrate multiplication
        print("Multiplication: 5 * 3 =", multiply(5, 3))
        
        # demonstrate division
        print("Division: 5 / 3 =", divide(5, 3))
        
        # demonstrate modulus
        print("Modulus: 5 % 3 =", modulus(5, 3))
        
        # demonstrate exponentiation
        print("Exponentiation: 5 ** 3 =", exponentiate(5, 3))
        
        # demonstrate square root
        print("Square Root: sqrt(25) =", sqrt(25))

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
