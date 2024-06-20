def tinh_min(matrix, row, col):
    del_cost = matrix[row-1][col] + 1
    ins_cost = matrix[row][col-1] + 1
    replace_value = 1
    if matrix[row][0] == matrix[0][col]:
        replace_value = 0
    rep_cost = matrix[row-1][col-1] + replace_value
    min_value = min([del_cost, ins_cost, rep_cost])
    return min_value

def khoang_cach_levenshtein(source, target):
    len_source = len(source)
    len_target = len(target)
    rows = len_source + 2
    cols = len_target + 2
    i_target = 2
    i_source = 2
    matrix = [[0]*cols for _ in range(rows)]
    matrix[0][0] = "?"
    matrix[0][1] = "#"
    matrix[1][0] = "#"
    for chu_cai in target:
        matrix[0][i_target] = chu_cai
        i_target += 1
    for chu_cai in source:
        matrix[i_source][0] = chu_cai
        i_source += 1
    for col in range(1, cols):
        matrix[1][col] = col - 1
    for row in range(1, rows):
        matrix[row][1] = row - 1
    for row in range(2, rows):
        for col in range(2, cols):
            matrix[row][col] = tinh_min(matrix, row, col)

    return matrix[rows-1][rows-1]

source = "yu"
target = "you"
ket_qua_cuoi = khoang_cach_levenshtein(source, target)
print(ket_qua_cuoi)