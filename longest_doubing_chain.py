def initialize_doubling_table(x):
    n = len(x)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][i] = 1

    for i in range(n):
        for j in range(i + 1, n):
            table[i][j] = 1 if 2 * x[i] <= x[j] else 0

    return table


def calculate_paths(table):
    length_table = len(table)
    for i in range(1, length_table):
        possible_paths = []
        for j in range(i):
            if table[j][i] != 0:
                p = table[j][j] + 1
                table[j][i] = p
                possible_paths.append(p)

        if possible_paths:
            table[i][i] = max(possible_paths)


def find_max_path_indexes(table):
    n = len(table)
    max_length = 0
    max_index = 0
    for i in range(n):
        if table[i][i] > max_length:
            max_index = i
            max_length = table[i][i]

    result_indices = [0] * max_length
    while True:
        result_indices[max_length - 1] = max_index
        for i in range(max_index - 1, -1, -1):
            if table[i][max_index] == max_length:
                max_length -= 1
                max_index = i
                break
        if max_length <= 1:
            result_indices[0] = max_index
            break

    return result_indices


def longest_doubling_chain(x):
    doubling_table = initialize_doubling_table(x)
    calculate_paths(doubling_table)
    return find_max_path_indexes(doubling_table)


x1 = [12, 3, 6, 26, 18, 50, 7]
print(longest_doubling_chain(x1))
