#!/usr/bin/python3

''' A Method that prints pascal_triangle

n : number of rows'''


def pascal_triangle(n):
    ''' returns n number of rows for pascal triangle'''
    # Initialize an empty list to store the rows of Pascal's triangle.
    triangle = []

    if n <= 0:
        return []  # Return an empty list for n <= 0.

    # Create the first row with a single element (1).
    triangle.append([1])

    for i in range(1, n):
        row = []  # Initialize an empty list for the current row.
        row.append(1)  # The first element is always 1.

        for j in range(1, i):
            # Compute the value at row[j].
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)  # Append the computed value to the current row.

        row.append(1)  # The last element is always 1.
        triangle.append(row)  # Append the current row to the triangle.

    return triangle  # Return the Pascal's triangle.
