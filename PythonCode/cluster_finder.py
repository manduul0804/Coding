import numpy as np

table1 = np.array([[1.0, 0.10, 0.41, 0.55, 0.35],
                   [0.1, 1.0, 0.64, 0.47, 0.98],
                   [0.41, 0.64, 1.0, 0.44, 0.85],
                   [0.55, 0.47, 0.44, 1.0, 0.76],
                   [0.35, 0.98, 0.85, 0.76, 1.0]])
print(table1[1][1])
print(table1.size)
print(table1.shape)

row, col = table1.shape

print(f'row: {row}')
print(f'col: {col}')

remaining_list = []
for i in range(row):
    remaining_list.append(i)

stored_list = []
listSize = 0
maxCol = 0
maxRow = 0
maxVal = 1
# Find the most simillar
for x in range(row):
    count = 0
    for i in range(row):
        for j in range(col):
            if (i != j and count <= table1[i][j] and maxVal > table1[i][j]):
                count = table1[i][j]
                maxRow = i
                maxCol = j
    print(f"row: {maxRow}  col: {maxCol}")
    table1[maxRow][maxCol] = maxVal
    table1[maxCol][maxRow] = maxVal
    stored_list.append(maxRow)
    stored_list.append(maxCol)
    stored_list = list(set(stored_list))

    
    for i in remaining_list[:]:
        for i in stored_list:
            remaining_list.remove(i)
    newCount = 0
    maxCol1 = 0
    maxRow1 = 0
    for i in remaining_list:
        print(f"printing i: {i}")
        for j in stored_list:

            if ((i != j) and newCount <=table1[i][j]):
                newCount = table1[i][j]
                maxCol1 = i
                maxRow1 = j
            else:
                newCount = table1[i][j]
        for n in stored_list:
            table1[i][n] = newCount
            table1[n][i] = newCount

    print("remaining lists: ")
    print(remaining_list)
    print("stored list")
    print(stored_list)

    print(table1)
    print("\n\n")

# print(f"count: {count} row: {maxRow+1} col: {maxCol+1} table: {table1[maxRow][maxCol]}")