import math

def tinh_can(so_can_tinh, can_bac=2):
    return math.pow(so_can_tinh, 1/can_bac)

print(tinh_can(9))

def md_nre(y, y_hat, n=2, p=1):
    ket_qua = ((tinh_can(y, n)) - (tinh_can(y_hat, n)))**p
    return ket_qua

print(md_nre(0.6, 0.1))