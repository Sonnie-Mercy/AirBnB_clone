def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average


def print_average(numbers):
    """Print the average of a list of numbers."""
    average = calculate_average(numbers)
    print(f"The average is: {average:.2f}")


def main():
    """Main function."""
    numbers = [1, 2, 3, 4, 5]
    print_average(numbers)


if __name__ == "__main__":
    main()
