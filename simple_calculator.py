def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """subtract second number from First"""
    return x - y

def multiply(x, y):
    """mulitply two numbers"""
    return x * y

def division(x, y):
    """divide first number with second"""
    if y == 0:
        return "Error! cannot divide by zero"
    return x / y

def floor_division(x, y):
    """floor divide first with second"""
    if y == 0:
        return "Error! cannot divide by zero"
    return x // y

def calculator():
    message = "Simple calculator started"
    print(message)
    
    while True:
        print("\n--- operations ---")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. division")
        print("5. floor_division")
        print("6. exit")
        
        choice = input("Choose your operation (1/2/3/4/5/6): ")
        
        match choice:
            case '6': 
                print("Calculator is closing! Thank you")
                break  # Stops the loop and ends the program safely
                
            case '1' | '2' | '3' | '4' | '5':
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("❌ Invalid input! please enter numbers only.")
                    continue  # Skips the rest of the loop and restarts it

                match choice:
                    case '1':
                        result = add(num1, num2)
                        operation_sign = "+" 
                    case '2':
                        result = subtract(num1, num2)
                        operation_sign = "-" 
                    case '3':
                        result = multiply(num1, num2)
                        operation_sign = "*"
                    case '4':
                        result = division(num1, num2)
                        operation_sign = "/"
                    case '5':
                        result = floor_division(num1, num2)
                        operation_sign = "//"
                
                # This print statement must sit outside the inner match-case 
                # so it can print the results for options 1, 2, 3, 4, and 5!
                print(f"{num1} {operation_sign} {num2} = {result}")
                
            case _:  # Notice the space before the underscore
                print("⚠️ Invalid choice! please enter a number from 1 to 6")

# Call the function to run the application
calculator()
