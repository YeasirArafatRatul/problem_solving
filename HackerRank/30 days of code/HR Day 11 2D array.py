array = []
maximum = min 
for _ in range(6):
    elements = [int(x) for x in str(input()).split(" ")]
    array.append(elements)
    
maximum = 10 ** -7 #0 will be okey too

for r in range(4):
    for c in range(1,5):
        add = array[r][c] + array[r][c + 1] + array[r][c + 2] + array[r + 1][c + 1] + array[r + 2][c] + array[r + 2][c + 1] + array[r + 2][c + 2]
            if add > maximum:
                maximum = add

print(maximum)

    
