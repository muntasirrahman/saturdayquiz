def right_sum(matr, target_values):
    n = len(matr)
    m = len(matr[0])

    next_row, next_col = False, False

    for i in range(0, n):
        next_row = i < (n - 1)

        for j in range(0, m):
            next_col = j < (m - 1)

            if next_row and next_col:
                right = matr[i][j+1]
                down = matr[i+1][j]
                print(f'c({i},{j}) > {right}, v {down}')

            elif next_col:
                right = matr[i][j + 1]
                print(f'c({i},{j}) > {right}')

            elif next_row:
                down = matr[i + 1][j]
                print(f'c({i},{j}) v {down}')

            else:
                print('Ends here')


if __name__ == '__main__':
    # matrices = [[1, 2],
    #             [3, 5]]
    matrices = [[1, 2, 4],
                [3, 5, 9],
                [6, 11, 20]]
    right_sum(matrices, [65, 72, 90, 110])
