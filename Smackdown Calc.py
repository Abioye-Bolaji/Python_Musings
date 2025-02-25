def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y ==0:
        return "Error: division by zero"
    return x / y

print("Welcome to the Smackdown Calculator!🔥🚀")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:
    choice = input("Enter your desired number (1/2/3/4) or 'Q' to quit: ")

    if choice.lower() == 'q':
        print("Goodbye!👋")
        break

    if choice in ('1', '2', '3', '4'):
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
