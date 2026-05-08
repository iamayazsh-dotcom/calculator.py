print("Simple Calculator  main.zip.py:1 - calculator.py:1")
print("")

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:  main.zip.py:8 - calculator.py:8")
    print("1. Add  main.zip.py:9 - calculator.py:9")
    print("2. Subtract  main.zip.py:10 - calculator.py:10")
    print("3. Multiply  main.zip.py:11 - calculator.py:11")
    print("4. Divide  main.zip.py:12 - calculator.py:12")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Answer =  main.zip.py:17 - calculator.py:17", num1 + num2)
    elif choice == '2':
        print("Answer =  main.zip.py:19 - calculator.py:19", num1 - num2)
    elif choice == '3':
        print("Answer =  main.zip.py:21 - calculator.py:21", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error! Can't divide by zero.  main.zip.py:24 - calculator.py:24")
        else:
            print("Answer =  main.zip.py:26 - calculator.py:26", num1 / num2)
    else:
        print("Invalid choice!  main.zip.py:28 - calculator.py:28")

    again = input("\nCalculate again? (yes/no): ")
    if again.lower() == 'no':
        print("Bye!  main.zip.py:32 - calculator.py:32")
        break
