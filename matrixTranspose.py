rows= int(input("enter the number of rows"))
cols = int(input("enter the number of columns"))
transpose=[]
matrix =[]
for i in range(rows):
    row=[]
    for j in range(cols):
        value= int(input(f"enter the number at ({i}{j})"))
        row.append(value)
    matrix.append(row)
print("Actual array")
for row in matrix:
    print(row)

for i in range(cols):
    new=[]
    for j in range(rows):
        new.append(matrix[j][i])
    transpose.append(new)
print("  Transpose matrix  ")
for row in transpose:
    print(row)


    # Rotate array 90 degree 
n= rows
rotated = []
for _ in range(cols):
    rotated.append([0] * rows)
    
for i in range(rows):
    for j in range(cols):
        rotated[j][n-i-1]= matrix[i][j]

print("After 90 degree rootate")
for row in rotated:
    print(row)


# 180 degrees
    
print("180 degree rotated array")

rotated1=[]
for i in range(rows):
    rotated1.append([0]*cols)

for i in range(rows):
    for j in range(cols):
        rotated1[rows-i-1][cols-j-1] = matrix[i][j]
for row in rotated1:
    print(row)