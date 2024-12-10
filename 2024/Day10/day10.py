import sys
from collections import deque, defaultdict

def parse_input(file_name):
    """Parse the input topographic map."""
    with open(file_name, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

# Part 1: Calculate Total Score Using BFS
def bfs(map_data, start):
    """
    Perform BFS from a trailhead.
    Returns a set of reachable '9' positions.
    """
    rows, cols = len(map_data), len(map_data[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()
    
    while queue:
        r, c = queue.popleft()
        
        # If we reached a '9', add to reachable set
        if map_data[r][c] == 9:
            reachable_nines.add((r, c))
        
        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Only move if the height difference is exactly +1
                if map_data[nr][nc] == map_data[r][c] + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    return reachable_nines

def calculate_trailhead_scores(map_data):
    """Calculate the total score of all trailheads."""
    rows, cols = len(map_data), len(map_data[0])
    total_score = 0
    
    for r in range(rows):
        for c in range(cols):
            if map_data[r][c] == 0:  # Found a trailhead
                reachable_nines = bfs(map_data, (r, c))
                total_score += len(reachable_nines)
    
    return total_score

# Part 2: Calculate Total Rating Using DFS
def dfs_count_trails(map_data, r, c, memo):
    """
    Perform a DFS to count all distinct hiking trails from a given position.
    Uses memoization to avoid redundant calculations.
    """
    rows, cols = len(map_data), len(map_data[0])
    
    # If this position is memoized, return the stored result
    if (r, c) in memo:
        return memo[(r, c)]
    
    # If this is height 9, it marks the end of a trail
    if map_data[r][c] == 9:
        return 1
    
    # Explore all possible moves
    total_trails = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and map_data[nr][nc] == map_data[r][c] + 1:
            total_trails += dfs_count_trails(map_data, nr, nc, memo)
    
    # Store the result in the memoization dictionary
    memo[(r, c)] = total_trails
    return total_trails

def calculate_trailhead_ratings(map_data):
    """Calculate the total rating of all trailheads."""
    rows, cols = len(map_data), len(map_data[0])
    total_rating = 0
    memo = {}  # To store intermediate results of DFS
    
    for r in range(rows):
        for c in range(cols):
            if map_data[r][c] == 0:  # Found a trailhead
                total_rating += dfs_count_trails(map_data, r, c, memo)
    
    return total_rating

def main():
    # Read input file
    input_file = sys.argv[1] if len(sys.argv) > 1 else "day10.txt"
    map_data = parse_input(input_file)
    
    # Part 1: Calculate the total score
    total_score = calculate_trailhead_scores(map_data)
    print(f"Total Score of All Trailheads (Part 1): {total_score}")
    
    # Part 2: Calculate the total rating
    total_rating = calculate_trailhead_ratings(map_data)
    print(f"Total Rating of All Trailheads (Part 2): {total_rating}")

if __name__ == "__main__":
    main()
