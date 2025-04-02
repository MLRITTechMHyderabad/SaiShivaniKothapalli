rows = int(input("Enter no. of rows: "))  
cols = int(input("Enter no. of cols: "))  
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        n = int(input(f"Enter element ({i},{j}): "))
        row.append(n) 
    matrix.append(row)  
print("Transposed Matrix:")
for j in range(cols):  
    for i in range(rows):  
        print(matrix[i][j], end=" ")  
    print()  



