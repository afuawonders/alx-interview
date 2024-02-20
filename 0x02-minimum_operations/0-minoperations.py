#!/usr/bin/python3
'''
Given a number n, write a method that
calculates the fewest number of operations
needed to result in exactly n H characters
in the file.
'''


def minOperations(n):
    '''
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return
    '''
    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)
    return operations[n]
