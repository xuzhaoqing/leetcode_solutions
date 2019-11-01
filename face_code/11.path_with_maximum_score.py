# Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

# Don't include the first or final entry. You can only move either down or right at any point in time.

# Example 1:

# Input:
# [[5, 1],
#  [4, 5]]

# Output: 4
# Explanation:
# Possible paths:
# 5 → 1 → 5 => min value is 1
# 5 → 4 → 5 => min value is 4
# Return the max value among minimum values => max(4, 1) = 4.
# Example 2:

# Input:
# [[1, 2, 3]
#  [4, 5, 1]]

# Output: 4
# Explanation:
# Possible paths:
# 1-> 2 -> 3 -> 1
# 1-> 2 -> 5 -> 1
# 1-> 4 -> 5 -> 1
# So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
# Return the max of that, so 4.

def pathMaximumScore(matrix):
    if not matrix:
        return -1
    R,C = len(matrix), len(matrix[0])
    if R == 1 and C == 1:
        return matrix[R-1][C-1]

    dp = [[float('inf') for _ in range(C)] for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if row == 0 and col == 0:
                continue
            elif row == 0:
                dp[row][col] = min(dp[row][col-1],matrix[row][col])
            elif col == 0:
                dp[row][col] = min(dp[row-1][col], matrix[row][col])
            elif row == R-1 and col == C-1:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
            else:
                dp[row][col] = min(matrix[row][col],max(dp[row-1][col], dp[row][col-1]))
    return dp[R-1][C-1]
    

if __name__ == "__main__":
    input = [[1]]
    print(pathMaximumScore(input))