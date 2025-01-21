def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Improved Version with Exception Handling
def calculate_average_improved(numbers):
    try:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 0 #handle cases where non-numeric data is inputed 