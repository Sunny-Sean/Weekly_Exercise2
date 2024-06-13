import random
import math


def is_number(n):
    if isinstance(n, int):
        return True
    return False


def ex3():
    sample = input(
        "Input number of samples (integer number) which are generated: ")
    sample_int = int(sample)
    if is_number(sample_int):
        loss_name = input("Input loss name: ")
        if loss_name == "MAE":
            tong = 0
            for i in range(sample_int):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = abs(target - pred)
                tong = tong + loss
                print(f"loss name: {loss_name}, sample: {i}, pred: {
                      pred}, target: {target}, loss: {loss}")
            print(f"Final MSA: {tong/sample_int}")
        elif loss_name == "MSE":
            tong = 0
            for i in range(sample_int):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - pred)**2
                tong = tong + loss
                print(f"loss name: {loss_name}, sample: {i}, pred: {
                      pred}, target: {target}, loss: {loss}")
            print(f"Final MSE: {tong/sample_int}")
        elif loss_name == "RMSE":
            tong = 0
            for i in range(sample_int):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - pred)**2
                tong = tong + loss
                print(f"loss name: {loss_name}, sample: {i}, pred: {
                      pred}, target: {target}, loss: {loss}")
            print(f"Final MSE: {math.sqrt(tong/sample_int)}")
    else:
        print("number of samples must be an integer number")


ex3()
