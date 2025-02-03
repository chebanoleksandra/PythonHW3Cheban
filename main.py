#1
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
while num1 != num2:
    if num1>num2:
        print(f"\nIncorrect input.\nFirst number changed to {num2}\nSecond number changed to {num1}")
        temp = num1
        num1 = num2
        num2 = temp
    else:
        print("\nOdd numbers in this range: ")
        for i in range(num1, num2 + 1):
            if i % 2 != 0:
                print(i, end=" ")
        break
else:
    print("\nIncorrect input. The start and the end of the range cannot be the same.")
