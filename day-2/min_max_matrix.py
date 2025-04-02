rows = int(input("Enter number of rows: "))  
cols = int(input("Enter number of columns: "))  
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        n = int(input(f"Enter element ({i},{j}): "))
        row.append(n) 
    matrix.append(row)  
min_element = matrix[0][0]  
max_element = matrix[0][0]  
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
print("Matrix:")
for row in matrix:
    print(*row)  
print(f"Minimum Element: {min_element}")  
print(f"Maximum Element: {max_element}")  
