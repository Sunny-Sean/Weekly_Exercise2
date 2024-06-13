def is_number(n):
    if isinstance(n, int):
        return True
    return False


def ex1(tp, fp, fn):
    if is_number(tp) and is_number(fp) and not is_number(fn):
        print("fn must be int")
    elif is_number(tp) and not is_number(fp) and is_number(fn):
        print("fp must be int")

    elif not is_number(tp) and is_number(fp) and is_number(fn):
        print("tp must be int")

    else:
        if tp == 0 or fp == 0 or fn == 0:
            print("tp and fp and fn must be greater than zero")
            return
        precision = tp / (tp+fp)
        recall = tp / (tp+fn)
        f1_score = 2*((precision*recall)/(precision+recall))
        print(f"precision is {precision}")
        print(f"recall is {recall}")
        print(f"f1-score is {f1_score}")


ex1(tp=2, fp=3, fn=5)
