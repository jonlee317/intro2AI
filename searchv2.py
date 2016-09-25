# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

    
def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    openList = [[0, init[0], init[1]]]
    grid[init[0]][init[1]] = 1
    gCount = cost
    checkItem = openList.pop()
    
    while (checkItem[1] != goal[0]) or (checkItem[2] != goal[1]):
        checkItemInit = checkItem
        countMoves = 0
        for d in delta:
            if (checkItem[1] + d[0]) >= 0 and (checkItem[2] + d[1]) >= 0 and (checkItem[1] + d[0]) <len(grid) and (checkItem[2] + d[1]) < len(grid[0]):
                if grid[checkItem[1] + d[0]][checkItem[2] + d[1]] == 0:
                    grid[checkItem[1] + d[0]][checkItem[2] + d[1]] = 1
                    openList.append([checkItem[0]+cost, checkItem[1] + d[0],checkItem[2] + d[1]])
                    countMoves += 1

        if len(openList) != 0:
            checkItem = openList.pop(0)

        if checkItemInit == checkItem:
            return "fail"
            break

        path = checkItem

    return path
    
print (search(grid,init,goal,cost))