
# Complete the formingMagicSquare function below.
all_matrix = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
]
"""taking 3 inputs on each line with space seperation
and repeating it three times"""
s = [[int(i) for i in input().split(' ') for j in range(3)]]
"""converting the values into an array.
we have total 9 inouts that's why loopin 9 times"""
n = [s[i][j] for i in range(3) for j in range(3)]
total_sum = []
"""subtractiong each value with the list of 
solved arrays each value"""
for l in all_matrix:
    min_cost = [abs(n[i]-l[i]) for i in range(9)]
""" adding all the subtracted values each time for an array"""
total_sum.append(sum(min_cost))
"""from all the values that we got(8 actually),printing the minimum one"""
print(min(total_sum))
