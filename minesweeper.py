'''Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) 
represents a free space..
return a grid where each dash is replaced by a digit, indicating the nimber of mines immediateley adjsacent to the spot. 
The mines will return as a #.
input Example
[ ["-", "-", "-", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]
output Example
[ ["1", "1", "2", "#", "#"],
["1", "#", "3", "3", "2"],
["2", "4", "#", "2", "0"],
["1", "#", "#", "2", "0"],
["1", "2", "2", "1", "0"] ]
'''
def num_grid(grid):
    # Guard check for empty grids
    if not grid or not grid[0]:
        return []
        
    rows = len(grid)
    cols = len(grid[0])
    
    # Create an empty output matrix matching the dimensions of the input
    output = [["" for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            # If the current spot is already a mine, keep it as "#"
            if grid[r][c] == "#":
                output[r][c] = "#"
                continue
            
            # Count adjacent mines across all 8 surrounding cells
            mine_count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue  # Skip checking the active cell itself
                    
                    nr, nc = r + dr, c + dc
                    # Ensure neighbor coordinates stay inside the valid grid bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "#":
                            mine_count += 1
            
            # Replace the dash with the string value of the calculated count
            output[r][c] = str(mine_count)
            
    return output



if __name__ == "__main__":
    
    # 1. Define your starting grid data
    starting_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]
    
    print("--- Input Grid ---")
    for row in starting_grid:
        print(row)
        

    completed_board = num_grid(starting_grid)
    
    # 3. Print the final result neatly
    print("--- Output Grid ---")
    for row in completed_board:
        print(row)


