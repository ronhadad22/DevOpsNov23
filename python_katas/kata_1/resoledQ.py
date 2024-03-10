def are_characters_unique(input_string):
    return len(set(input_string)) == len(input_string)

# Example usage:
result = are_characters_unique("alex")
print(result)  # Output: False