# Determines whether a given move is valid: Checks 3 conditions
# 1. Is move in bounds? 2. Has the square been visited already? 3. Is the square == 1?
def valid_move(matrix, visited, x, y):
    if (x >= 0 and x <= 4 and y >= 0 and y <= 4) and not visited[x][y] and matrix[x][y] == 1:
        return True
    else: 
        return False

# Performs recursive, depth first search for island in matrix
def depth_first_search(matrix, visited, x, y):

    visited[x][y] = True

    neighbors = [(x - 1, y),     # Square to the left
                 (x + 1, y),     # Square to the right
                 (x + 1, y + 1), # Square to the right and up
                 (x + 1, y - 1), # Square to the right and down
                 (x - 1, y + 1), # Square to the left and up
                 (x - 1, y - 1), # Square to the left and down
                 (x, y - 1),     # Square above
                 (x, y + 1)]     # Square below

    # For each possible neighbor in the our neighbors list, check validity of square and search it
    for next_x, next_y in neighbors:
        if valid_move(matrix, visited, next_x, next_y):
            depth_first_search(matrix, visited, next_x, next_y)

def main():

    matrix = [[1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0]]

    visited = [ [ False for i in range(5) ] for j in range(5) ]

    number_of_islands = 0

    # For each row
    for i in range(4):
        # For each column
        for j in range(4):
            # If the square hasn't been visited & the square contains a 1
            if not visited[i][j] and matrix[i][j] == 1:
                number_of_islands += 1
                depth_first_search(matrix, visited, i, j)

    print(number_of_islands)
   

if __name__ == '__main__':
    main()
