#1
# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
# while num1 != num2:
#     if num1>num2:
#         print(f"\nIncorrect input.\nFirst number changed to {num2}\nSecond number changed to {num1}")
#         temp = num1
#         num1 = num2
#         num2 = temp
#     else:
#         print("\nOdd numbers in this range: ")
#         for i in range(num1, num2 + 1):
#             if i % 2 != 0:
#                 print(i, end=" ")
#         break
# else:
#     print("\nIncorrect input. The start and the end of the range cannot be the same.")

#2
num1 = 100
num2 = 9999
quantity = 0
while num1 <= num2:
    if num1>=1000:
        a = num1//1000
    b = (num1%1000)//100
    c = (num1%100)//10
    d = num1 % 10
    if b!= c and b!=d and c!=d:
        if num1>=1000:
            if a!=b and a!= c and a!=d:
                quantity += 1
        else:
            quantity+=1
    num1+=1
print(quantity)