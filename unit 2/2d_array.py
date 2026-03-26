# Creating a 2D array (2 rows and 3 columns)
matrix = [
    [1, 2, 3],   
    [4, 5, 6]    
]
# Printing entire matrix
print("Complete Matrix:")
print(matrix)

print("\nMatrix Elements Row by Row:")

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        print(matrix[i][j], end=" ")
        
    print()

print("\nAccess Specific Element:")

print("Element at row 1 column 2 is:", matrix[0][1])