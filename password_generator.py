import sys
import random
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mask')
    parser.add_argument('-c', '--count', type=int, default=1)

    return parser


def get_lower_symbol():
    return random.choice("wertyupasdfghkzxcvbnm")


def get_upper_symbol():
    return get_lower_symbol().upper()


def get_number():
    return random.choice("123456789")


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])

count = namespace.count
mask = namespace.mask

while count > 0:
    result = ''
    for ch in mask:
        if ch == 'n':
            result += get_number()
        elif ch == 'c':
            result += get_lower_symbol()
        elif ch == 'C':
            result += get_upper_symbol()
        else:
            print("Error in mask")
            sys.exit()

    print(result)
    count -= 1
