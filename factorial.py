def main():

    def valid_input():
        # Checks if user input is a valid input
        while True:
            try:
                number = int(input("Enter a whole number: "))
                if number < 0:
                    print("Please enter a positive integer.")
                    # If it is a negative number
                else:
                    return number
                # If it is not a number
            except ValueError:
                print("Invalid input. Please enter number.")

    # I wanted to try something fancier
    # Calculates factorial
    def calculate_factorial(number):

        # Sets factorial to 1
        factorial = 1
        user_number = 1

        # do while loop
        while True:
            # If user number is 0 set factorial to 1 and end program
            if number == 0:
                factorial = 1
                break
            # multiplies factorial by the user number (can also be factorial == factorial * user_number)
            factorial *= user_number
            # adds 1 to user number (can also be user_number = user_number + 1)
            user_number += 1
            # if user number is less than number then end the program
            if user_number > number:
                break
        return factorial

    # Takes the user input and sets it to 'number'
    number = valid_input()
    # Takes the answer and sets it to 'result'
    result = calculate_factorial(number)
    # Prints the factorial of 'number' is 'result'
    print(f"Factorial of {number} is {result}")


if __name__ == "__main__":
    main()
