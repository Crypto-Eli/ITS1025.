def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def get_positive_integer():
    """Returns a positive integer."""
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n < 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Please enter a positive integer.")
def generate_fibonacci(n):
    """Generates the fibonacci sequence up to n terms using iteration."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
def main():
    print("Welcome to the Fibonacci Sequence Program!")
    #get user input
    n = get_positive_integer()
    #print the nth Fibonacci number
    fib_sequence = generate_fibonacci(n)

    print(f"The first {n} terms of the Fibonacci sequence are: {fib_sequence}")
    print("the first {n}terms of the fibonacci seqence are: {fib_sequence}")

    if __name__== "__main__":
        main()
        
    
