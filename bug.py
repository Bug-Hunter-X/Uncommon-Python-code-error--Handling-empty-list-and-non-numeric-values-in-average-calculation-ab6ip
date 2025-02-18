def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list
    average = total / count
    return average

# Example usage with potential error:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#Example of a list with non-numeric values
my_list = [1,2,3,'a']
average = calculate_average(my_list)
print(f"The average is: {average}")