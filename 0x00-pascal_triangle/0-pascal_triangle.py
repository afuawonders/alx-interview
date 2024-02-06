#!/usr/bin/python3
"""
Pascal Trangle

"""def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of every row is 1

        if triangle:
            last_row = triangle[-1]
            # Generate elements from the second to second-to-last
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Last element of every row is 1

        triangle.append(row)

    return triangle

if __name__ == "__main__":
    pascal_triangle_result = pascal_triangle(5)

    for row in pascal_triangle_result:
        print("[{}]".format(",".join([str(x) for x in row])))
