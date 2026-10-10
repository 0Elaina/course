import numpy as np


def quadrant_means(matrix):
    mat = np.array(matrix)
    rows, cols = mat.shape

    if rows % 2 != 0 or cols % 2 != 0 or rows != cols:
        raise ValueError("矩阵必须是 2x2 方阵")

    n = rows // 2
    top_left_avg = np.mean(mat[:n, :n])
    top_right_avg = np.mean(mat[:n, n:])
    bottom_left_avg = np.mean(mat[n:, :n])
    bottom_right_avg = np.mean(mat[n:, n:])

    new_matrix = np.array(
        [[top_left_avg, top_right_avg], [bottom_left_avg, bottom_right_avg]]
    )

    return new_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 5, 7], [4, 1, 8, 0], [2, 0, 5, 1], [0, 2, 1, 1]]
    print(f"original_matrix: {matrix}\nnew_matrix: {quadrant_means(matrix)}")
