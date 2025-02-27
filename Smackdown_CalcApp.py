# Defining Arithmetic Operations

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: division by zero"
    return x / y

print("Welcome to the Smackdown Calculator!🔥🚀")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

invalid_response_count = 0 #Initializing the count of invalid responses to 0

while True:
    choice = input("Enter your desired number (1/2/3/4) or 'Q' to quit: ").strip()

    if choice.lower() == 'q':
        print("Goodbye!👋")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num_1, num_2))

            elif choice == '2':
                print("Result: ", sub(num_1, num_2))

            elif choice == '3':
                print("Result: ", mul(num_1, num_2))

            elif choice == '4':
                print("Result: ", div(num_1, num_2))
            
            invalid_response_count = 0  # Reset the count after a valid operation
        except ValueError:
            print("Error: Invalid number input. Please enter numeric values.")
    else:
        invalid_response_count += 1
        if invalid_response_count == 4:
            print("You entered an invalid response 4 times😥. Exiting program😔.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4 or 'Q' to quit.")