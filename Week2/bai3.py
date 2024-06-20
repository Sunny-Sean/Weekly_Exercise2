def tao_tu_dien(tu_dien, mang_tu):
    for tu in mang_tu:
        tu = tu.lower()
        if tu in tu_dien:
            tu_dien[tu] += 1
        else:
            tu_dien[tu] = 1
    return tu_dien

def read_data(file_name):
    with open(file_name, 'r') as file:
        tu_dien = {}
        contents = file.read()
        contents = contents.replace("\n", " ")
        noi_dung_tach = contents.split(" ")
        tu_dien_moi = tao_tu_dien(tu_dien, noi_dung_tach)
        file.close()
        return tu_dien_moi
    
file_name = "G:\AIO\Module_1\Weekly_Exercise\Week2\P1_data.txt"
dir_new = read_data(file_name)
print(dir_new)