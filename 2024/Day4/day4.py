def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Define all possible directions to look for the word: 
    # Horizontal (left and right), Vertical (up and down), 
    # and Diagonal (all four diagonals).
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1), # Diagonal Down-Left
        (-1, 1), # Diagonal Up-Right
        (-1, -1) # Diagonal Up-Left
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(word_len):
                    # Calculate new row and column indices
                    nr, nc = r + dr * i, c + dc * i
                    # Check if the new indices are out of bounds or if the character doesn't match
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                        found = False
                        break
                # If the word is found in the current direction, increment the count
                if found:
                    count += 1
    return count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_x_mas(r, c):
        # Ensure the center of the X-MAS pattern is not near the boundary
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False

        # Check for the X-MAS pattern:
        # - Top-left to bottom-right diagonal should have "M" at top-left and "S" at bottom-right,
        #   or vice versa ("S" at top-left and "M" at bottom-right).
        # - Top-right to bottom-left diagonal should have "M" at top-right and "S" at bottom-left,
        #   or vice versa ("S" at top-right and "M" at bottom-left).
        # - The center must always be "A".
        return (
            ((grid[r - 1][c - 1] == "M" and grid[r + 1][c + 1] == "S") or
             (grid[r - 1][c - 1] == "S" and grid[r + 1][c + 1] == "M")) and
            ((grid[r - 1][c + 1] == "M" and grid[r + 1][c - 1] == "S") or
             (grid[r - 1][c + 1] == "S" and grid[r + 1][c - 1] == "M")) and
            grid[r][c] == "A"
        )

    for r in range(1, rows - 1):  # Skip edges to avoid out-of-bounds errors
        for c in range(1, cols - 1):  # Skip edges to avoid out-of-bounds errors
            if is_x_mas(r, c):  # Check if an X-MAS pattern exists centered at (r, c)
                count += 1

    return count

def read_grid_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

file_path = "day4.txt"
grid = read_grid_from_file(file_path)
word = "XMAS"

# Count occurrences of the word XMAS in all directions
total_occurrences = count_word_occurrences(grid, word)
print("Total occurrences of XMAS:", total_occurrences)

# Count occurrences of the X-MAS pattern
total_x_mas = count_x_mas(grid)
print("Total occurrences of X-MAS:", total_x_mas)
