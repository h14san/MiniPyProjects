def main_menu():
    print("-------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. History")
    print("6. Quit")
    print("-------------------")
def get_number(input_text):
    while True:
        try:
            value = int(input(input_text))
            return value
        except ValueError:
            print("Invalid number")
history = []
while True:
    main_menu()
    choice = get_number(input_text="Choose an operation: ")
    if choice > 6:
        print("Invalid!! Retry")
        continue
    elif choice == 6:
        break
    elif choice == 5:
        for i in range(len(history)):
            print(f"{i+1}) {history[i]}")
        continue
    num1 = get_number(input_text="Number1- ")
    num2 = get_number(input_text="Number2- ")
    res = 0
    sign = ""
    if choice == 1:
        res = num1 + num2
        sign = "+"
    elif choice == 2:
        res = num1 - num2
        sign = "-"
    elif choice == 3:
        res = num1 * num2
        sign = "*"
    elif choice == 4:
        res = num1 / num2
        sign = "/"
    operation = f"{num1} {sign} {num2} = {res}"
    print(operation)
    history.append(operation)
    if len(history) > 5:
        del history[0]