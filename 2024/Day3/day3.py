import re

# Part 1

def extract_and_sum_mul_instructions(file_path):
    with open(file_path, "r") as file:
        memory = file.read()
    
    pattern = r"mul\((\d+),(\d+)\)"
    
    matches = re.findall(pattern, memory)
    
    total = sum(int(x) * int(y) for x, y in matches)
    
    return total


def extract_and_sum_mul_instructions_with_conditions(file_path):
    with open(file_path, "r") as file:
        memory = file.read()
    
    mul_pattern = r"mul\((\d+),(\d+)\)"
    condition_pattern = r"(do\(\)|don't\(\))"
    
    instructions = re.finditer(f"{condition_pattern}|{mul_pattern}", memory)
    
    mul_enabled = True  # Multiplication is initially enabled
    total = 0
    
    for instruction in instructions:
        if instruction.group(1):
            if instruction.group(1) == "do()":
                mul_enabled = True
            elif instruction.group(1) == "don't()":
                mul_enabled = False
        elif instruction.group(2) and instruction.group(3):
            if mul_enabled:
                x, y = int(instruction.group(2)), int(instruction.group(3))
                total += x * y
    
    return total


file_path = "day3.txt"

# Process the file to calculate the sum of valid mul instructions
part1 = extract_and_sum_mul_instructions(file_path)
part2 = extract_and_sum_mul_instructions_with_conditions(file_path)

print("Total sum of enabled mul instructions:", part1)

# Print the result
print("Total sum of valid mul instructions:", part2)


