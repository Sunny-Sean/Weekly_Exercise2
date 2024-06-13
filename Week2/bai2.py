def count_chars(chuoi):
    thu_vien = {}

    for ky_tu in chuoi:
        ky_tu = ky_tu.lower()
        if ky_tu in thu_vien:
            thu_vien[ky_tu] += 1
        else:
            thu_vien[ky_tu] = 1
    return thu_vien


chuoi = "SMmilesSIm"
print(count_chars(chuoi))
