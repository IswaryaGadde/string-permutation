#Iswarya (13-10-2023) string permutations

#Test Case: Permutations of the string will be n! as per that we should get all permutations.

def get_permutations(input_str):
    permutations = []
    generate_permutations('', input_str)
    return permutations

def generate_permutations(current, remaining):
        if not remaining:
            permutations.append(current)
            return

        for i in range(len(remaining)):
            next_char = remaining[i]
            new_current = current + next_char
            new_remaining = remaining[:i] + remaining[i+1:]
            generate_permutations(new_current, new_remaining)



input_str = str(input('Enter input:'))
permutations = get_permutations(input_str)

for perm in permutations:
    print(perm)

