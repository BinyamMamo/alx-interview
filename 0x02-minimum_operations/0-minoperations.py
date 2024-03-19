#!/usr/bin/python3
"""
Task 0 - Minimum Operations

In a text file, there is a single character H. Your text editor can execute
only two operations in this file: `Copy All` and `Paste`. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to get `n` 'H' characters.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n//i)
    return n

# Example usage
if __name__ == "__main__":
    n1 = 4
    n2 = 12
    print(f"Min # of operations to reach {n1} char: {minOperations(n1)}")
    print(f"Min # of operations to reach {n2} char: {minOperations(n2)}")