#!/usr/bin/env python3

'''
Algorithm 1: Walls of Maria and the Titans
Ellie Winter 
'''

from collections import deque
import numpy as np


def find_inf_indices(matrix):
    '''Find the indices of the 'INF' values in the matrix'''
    inf_instances = np.where(matrix == 'INF')
    inf_indices = list(zip(inf_instances[0].tolist(), inf_instances[1].tolist()))
    return inf_indices


def bfs_shortest_path(matrix, start):
    '''Breadth-first search to find the shortest path'''
    num_rows, num_cols = matrix.shape
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col, steps = queue.popleft()

        if matrix[row][col] == 0:
            return steps

        for dir_row, dir_col in directions:
            new_row, new_col = row + dir_row, col + dir_col

            if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
                (new_row, new_col) not in visited and matrix[new_row, new_col] != -1):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))

    return -1


def build_new_matrix(matrix):
    '''Build a new matrix with the shortest path to 0 from each 'INF' value'''
    numeric_matrix = np.where(matrix == 'INF', 9999, matrix).astype(int)

    result_matrix = numeric_matrix.copy()

    inf_indicies = find_inf_indices(matrix)

    for idx in inf_indicies:
        result_matrix[idx] = bfs_shortest_path(numeric_matrix, idx)

    return result_matrix


def main():
    '''Main function'''
    custom = input('''Welcome to Walls of Maria and the Titans!'Would you like
    to use the example matricies or enter in your own? 
    Type "e" for the example or "c" for custom:''')
    if custom == 'e':
        sample_1 = np.array([['INF', -1, 0, 'INF'],
                    ['INF', 'INF', 'INF', -1],
                    ['INF', -1, 'INF', -1],
                    [0, -1, 'INF', 'INF']], dtype=object)

        print('Sample 1 Result:')
        print(build_new_matrix(sample_1))

        print('Sample 2 Result:')
        sample_2 = np.array([[0, 'INF', 'INF'],
                    ['INF', -1, 'INF'],
                    ['INF', 'INF', 0]], dtype=object)

        print(build_new_matrix(sample_2))
    elif custom == 'c':
        print('You have chosen to enter in your own matrix.')
        num_rows = int(input('Enter the number of rows: '))
        num_cols = int(input('Enter the number of columns: '))
        custom_matrix = np.empty((num_rows, num_cols), dtype=object)
        valid_values = ['0', '-1', 'INF']
        for i in range(num_rows):
            for j in range(num_cols):
                while True:
                    value = input(f'Enter the value for row {i + 1} and column {j + 1} (0, -1, or INF): ')
                    if value in valid_values:
                        custom_matrix[i][j] = value if value == 'INF' else int(value)
                        break
                    print('Invalid input. Please enter only 0, -1, or INF.')

        print('You have entered the following matrix:')
        print(custom_matrix)

        print('Result:')
        print(build_new_matrix(custom_matrix))
    else:
        print('Invalid input. Please enter "e" or "c".')
        return -1

    return 0


if __name__ == '__main__':
    main()
