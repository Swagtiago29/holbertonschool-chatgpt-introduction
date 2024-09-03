#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <non-negative integer>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
    except ValueError as e:
        print(e)
        sys.exit(1)

    f = factorial(n)
    print(f)

if __name__ == "__main__":
    main()
