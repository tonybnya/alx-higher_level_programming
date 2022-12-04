#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    usage = "Usage: ./100-my_calculator.py <a> operator <b>"
    error = "Unknow operator. Available operators: +, -, * and /"
    errordiv = "Error: Division by 0"
    args = len(argv[1:])

    if args != 3:
        print("{}".format(usage))
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            if b == 0:
                print("{}".format(errordiv))
                exit(1)
            else:
                print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("{}".format(error))
            exit(1)
