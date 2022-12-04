#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    usage = "Usage: ./100-my_calculator.py <a> operator <b>"
    error = "Unknow operator. Available operators: +, -, * and /"
    errordiv = "Error: Division by 0"
    args = len(sys.argv[1:])

    if args != 3:
        print("{}".format(usage))
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        if b == 0:
    	    print("{}".format(errordiv))
    	    sys.exit(1)

        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("{}".format(error))
        sys.exit(1)
