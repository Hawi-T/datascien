def find_largest(numbers):
    # Handle empty list case
    if not numbers:
        return None
    
    # Assume the first number is the largest initially
    largest = numbers[0]
    
    # Iterate through the rest of the list
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if a bigger number is found
            
    return largest

# Testing the function
my_list = [15, 72, 5, 88, 23]
result = find_largest(my_list)
print(f"The largest number is: {result}")