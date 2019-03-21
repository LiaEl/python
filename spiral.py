n = int(input())

x, y = 0, 0 # base coordinates
step_x, step_y = 0, 1 # steps for X and Y
spiral = [[None] * n for _ in range(n)] # empty array

for i in range(1, n ** 2 + 1):
    spiral[x][y] = i # fill the array
    next_x, next_y = x + step_x, y + step_y # create next cell

    if 0 <= next_x < n and 0 <= next_y < n and spiral[next_x][next_y] == None: # check next cell is exist and empty
        x += step_x
        y += step_y
    else:
        step_x, step_y = step_y, -step_x # change direction
        x += step_x
        y += step_y

for x in range(n):
    for y in range(n):
        print(spiral[x][y], end=' ')
    print()