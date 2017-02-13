import sys
import random


def get_symbol():
    return random.choice("wertyupasdfghkzxcvbnm")


def get_number():
    return random.choice("123456789")


amount = int(input("Please input the amount of passwords: "))
print("Mask may contents symbols: c - character, n - number")
mask = input("Please input the mask for passwords: ")

print("Start list of passwords")

while amount > 0:
    result = ''
    for ch in mask:
        if ch == 'n':
            result += get_number()
        elif ch == 'c':
            result += get_symbol()
        else:
            print("Error in mask")
            sys.exit()

    print(result)
    amount -= 1

print("End list of passwords")

