from itertools import permutations

def generate_arrangements(row, damaged_groups):
    arrangements = set()

    def backtrack(index, arrangement, remaining_numbers):
        if index == len(row):
            arrangements.add(''.join(arrangement))
            return

        if row[index] == '?':
            for spring in '.#':
                arrangement[index] = spring
                backtrack(index + 1, arrangement, remaining_numbers)
        else:
            arrangement[index] = row[index]
            backtrack(index + 1, arrangement, remaining_numbers)

    def is_valid(arrangement):
        current_group_size = 0
        current_group_index = 0

        for char in arrangement:
            if char == '#':
                current_group_size += 1
            elif char == '.' and current_group_size > 0:
                if current_group_size != damaged_groups[current_group_index]:
                    return False
                current_group_size = 0
                current_group_index += 1

        if current_group_size > 0:
            return current_group_size == damaged_groups[current_group_index]

        return True

    numbers_permutations = set(permutations("311"))

    for numbers in numbers_permutations:
        remaining_numbers = list(numbers)
        backtrack(0, [' '] * len(row), remaining_numbers)

    valid_arrangements = set()

    for arrangement in arrangements:
        if is_valid(arrangement):
            valid_arrangements.add(arrangement)

    return valid_arrangements

# Example usage:
row = '??###????.???'
damaged_groups = [3,1,1]
result = generate_arrangements(row, damaged_groups)
print("Number of valid arrangements:", len(result))
print("Valid arrangements:", result)