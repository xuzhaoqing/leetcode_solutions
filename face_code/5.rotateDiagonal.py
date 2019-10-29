# Rotate matrix with diagonals
# k 代表次数
def rotateDiagonal(matrix,k):
    n = len(matrix)
    for _ in range(k):
        for i in range(len(matrix)):
            for j in range(i):
                if i != j and i + j != len(matrix) - 1:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    for i in range(len(matrix)):
        for j in range(len(matrix) // 2):
            if i != j and i + j != len(matrix) - 1:
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    rotateDiagonal(matrix,k)
    print(matrix)