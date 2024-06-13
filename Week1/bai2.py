import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def ex2():
    value_x = input("Input x = ")
    if is_number(value_x):
        value = float(value_x)
        thuc_hien = input("Input activation Function (sigmoid|relu|elu): ")
        if thuc_hien == "sigmoid":
            sigmoid = 1 / (1+math.e**(-value))
            print(sigmoid)
            return sigmoid
        elif thuc_hien == "relu":
            if value <= 0:
                relu = 0
            else:
                relu = value
            print(relu)
            return relu
        elif thuc_hien == "elu":
            if value <= 0:
                elu = 0.01*((math.e**value)-1)
            else:
                elu = value
            print(elu)
            return elu
        else:
            print(f"{thuc_hien} is not supported")

    else:
        print("x must be a number")


ex2()
