def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage with error handling:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 0

my_list = [1, 2, 3, 'a']
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 2.0

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}") # Output:3.0