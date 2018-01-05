multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([x[1] for x in multiList])
print([multiList[i][i] for i in range(len(multiList))])