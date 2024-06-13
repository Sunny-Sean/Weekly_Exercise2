def is_number(n):
    if isinstance(n, int):
        return True
    return False

def sliding_window_max(list_ban_dau, k):
    for i in list_ban_dau:
        if not is_number(i):
            return
    if k <= 0:
        return
    list_ket_qua = []
    list_k_phan_tu = []
    len_list_k = 0
    dieu_kien = True
    while dieu_kien:
        for i in range(len_list_k, len_list_k + k):
            list_k_phan_tu.append(list_ban_dau[i])
        phan_tu_max_trong_list_k = max(list_k_phan_tu)
        list_ket_qua.append(phan_tu_max_trong_list_k)
        len_list_k = len_list_k + 1
        list_k_phan_tu = []
        if len_list_k == len(list_ban_dau) - (k-1):
            dieu_kien = False
    print(list_ket_qua)


print(is_number("77"))

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

sliding_window_max(num_list, k)