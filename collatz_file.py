# Collatz sequence

def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return num * 3 + 1
    else:
        print("something went wrong in collatz")


print("Enter the number for collatz sequence : ")
number = int(input())
print("The collatz sequence are :")
print(number)

while number != 1:
    number = collatz(number)
    print(number)
