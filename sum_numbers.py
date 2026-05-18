"""
Basic Python Program for Sum of User Input Numbers
This program takes numbers as input from the user and calculates their sum.
"""

def sum_of_numbers():
    """
    Function to calculate the sum of user input numbers.
    User can enter numbers one by one and type 'done', 'exit', or 'q' to finish.
    """
    numbers = []
    count = 0
    
    print("=" * 50)
    print("Sum of User Input Numbers")
    print("=" * 50)
    print("Enter numbers one by one.")
    print("Type 'done', 'exit', or 'q' to finish.\n")
    
    while True:
        try:
            user_input = input(f"Enter number {count + 1}: ").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ['done', 'exit', 'q']:
                if count == 0:
                    print("\nNo numbers entered!")
                    return
                break
            
            # Convert input to float
            number = float(user_input)
            numbers.append(number)
            count += 1
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
    
    # Calculate results
    total_sum = sum(numbers)
    average = total_sum / count
    
    # Display results
    print("\n" + "=" * 50)
    print("Results:")
    print("=" * 50)
    print(f"Total numbers entered: {count}")
    print(f"Sum of numbers: {total_sum}")
    print(f"Average: {average:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    sum_of_numbers()
