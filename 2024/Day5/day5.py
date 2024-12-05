from collections import defaultdict, deque

def parse_input(file_path):
    """
    Parses the input file into rules and updates.
    """
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
    
    rules = []
    updates = []
    for line in lines:
        if "|" in line:
            x, y = map(int, line.split("|"))
            rules.append((x, y))
        elif line.strip():
            updates.append(list(map(int, line.split(","))))
    
    return rules, updates


def is_update_order_valid(update, rules):
    """
    Checks if an update is valid based on the rules.
    """
    position = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False
    return True


def get_middle_number(update):
    """
    Returns the middle number of the update.
    """
    return update[len(update) // 2]


def topological_sort_with_subset(rules, update):
    """
    Returns the topological order of the given update pages, 
    considering only the relevant rules.
    """
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for x, y in rules:
        if x in update_set and y in update_set:
            adj[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages


def correct_order_for_update(update, rules):
    """
    Correctly orders a given update using a subset of the topological rules.
    """
    ordered_pages = topological_sort_with_subset(rules, update)
    page_position = {page: idx for idx, page in enumerate(ordered_pages)}
    return sorted(update, key=lambda page: page_position.get(page, float('inf')))


def main():
    """
    Main function to parse input, validate updates, fix incorrect updates, and calculate the result.
    """
    file_path = "day5.txt"  # Ensure this file exists and is properly formatted
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        if is_update_order_valid(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    # Part 1: Middle numbers of valid updates
    middle_sum_valid = sum(get_middle_number(update) for update in valid_updates)
    print("Part 1 - Sum of middle page numbers for valid updates:", middle_sum_valid)
    
    # Part 2: Middle numbers of corrected invalid updates
    middle_sum_invalid = 0
    for update in invalid_updates:
        correct_update = correct_order_for_update(update, rules)
        middle_sum_invalid += get_middle_number(correct_update)
    
    print("Part 2 - Sum of middle page numbers for corrected invalid updates:", middle_sum_invalid)


if __name__ == "__main__":
    main()
