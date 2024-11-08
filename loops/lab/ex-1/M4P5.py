# Task 1:
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Enter a number")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            number = input("Enter a number: ")
            if not number.isdigit() or (number[0] == '-'):
                print("Invalid input. Please enter an integer.")
                continue

            digits = [int(d) for d in str(number)]
            count_digits = len(digits)
            summary_digits = sum(digits)
            average_digits = summary_digits / count_digits
            zero_count = str(number).count('0')

            print(f"\nNumber of digits: {count_digits}")
            print(f"Summary of digits: {summary_digits}")
            print(f"Average of digits: {average_digits}")
            print(f"Number of zeros: {zero_count}")

        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

main_menu()

# Task 2:
cell_size = 8
board_size = 8

for row in range(board_size):

    for line in range(round(cell_size/2)):
        row_pattern = ""

        start_with_filled = (row % 2 == 0)

        for col in range(board_size):
            if (col % 2 == 0) == start_with_filled:
                row_pattern += '*' * cell_size
            else:
                row_pattern += '-' * cell_size

        print(row_pattern)

# Task 3:
import random


def multiplication_test(level):
    score = 0
    if level == 1:
        num_questions = 5
        max_num = 10
    elif level == 2:
        num_questions = 10
        max_num = 15
    else:
        num_questions = 15
        max_num = 20

    for i in range(num_questions):
        # Generate two random numbers for the multiplication question
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        correct_answer = num1 * num2

        # Ask the user for their answer
        user_answer = int(input(f"What is {num1} x {num2}? "))

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    # Output the user's score
    print(f"\nYou got {score} out of {num_questions} correct.")
    percentage = (score / num_questions) * 100
    print(f"Your score: {percentage}%")

    if percentage == 100:
        print("Excellent! You mastered the multiplication table!")
    elif percentage >= 75:
        print("Good job! Keep practicing to improve.")
    elif percentage >= 50:
        print("Not bad, but you should practice more.")
    else:
        print("Keep working on it! You'll get better with practice.")


def main():
    print("\nWelcome to the multiplication table test!")
    print("\nChoose a difficulty level:")
    print("1. Easy (1-10 multiplication, questions number 5)")
    print("2. Medium (1-15 multiplication, questions number 10)")
    print("3. Hard (1-20 multiplication, questions number 15)")

    while True:
            level = int(input("\nEnter the difficulty level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                break
            else:
                print("\nPlease enter a valid level.")

    multiplication_test(level)

main()

# Task 4:
print()
def print_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = 12
print_diamond(n)