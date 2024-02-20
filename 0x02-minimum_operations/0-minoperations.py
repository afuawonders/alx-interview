#!/usr/bin/python3
'''Calculates the fewest number of operations needed to get exactly n H characters'''

def minOperations(n):
    '''Returns 0 if n is impossible to achieve'''
    pasted_chars = 1  # chars in the file
    clipboard = 0  # H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        if clipboard == 0:  # if not copied yet
            clipboard = pasted_chars  # copy all
            counter += 1  # increment counter

        if pasted_chars == 1:  # if not pasted yet
            pasted_chars += clipboard  # paste
            counter += 1  # increment counter
            continue  # continue loop

        remaining = n - pasted_chars  # remaining chars to paste
        if remaining < clipboard:  # check if impossible
            return 0  # return 0

        if remaining % pasted_chars != 0:  # if can't be divided
            pasted_chars += clipboard  # paste current clipboard
            counter += 1  # increment counter
        else:
            clipboard = pasted_chars  # copy all
            pasted_chars += clipboard  # paste
            counter += 2  # increment counter

    if pasted_chars == n:  # if got desired result
        return counter
    else:
        return 0
