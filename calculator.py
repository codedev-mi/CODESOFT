def calculator():
    while True:
     # Get user input
        user_input = input("Enter Operation: ")
        
        # Check if the user input is a valid operator
        if user_input in ["+", "-", "*", "/"]:
            # Get first number
            num1 = float(input("Enter First Number: "))
            # Get second number
            num2 = float(input("Enter Second Number: "))
         
            # Perform the operation based on the user input
            if user_input == "+":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
            # check if user wants another calculation
            # break the while loop if answer is no
            next_input = input("exit calculation? (yes/no): ")
            if next_input == "no":
              break
                
        else:
            # In case of invalid input
            print("Invalid Input")

# Call the calculator function to start the program
calculator()
