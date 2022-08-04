def value_in_triangle(i,j):
    if(j==1 or j==i):
        return 1
    return value_in_triangle(i-1,j-1)+value_in_triangle(i-1,j)

print(value_in_triangle(5,5))

