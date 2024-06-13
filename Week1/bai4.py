def giai_thua(n):
    tich = 1
    for i in range(n):
        tich = tich*(i+1)
    return tich

def approx_sin(x, n):
    tong = 0
    so_lan = n + 1
    for i in range(so_lan):
        sin = ((-1)**i)*((x**(2*i+1))/(giai_thua(2*i+1)))
        tong = tong + sin
    return tong

print(approx_sin(3.14, 10))

def approx_cos(x, n):
    tong = 0
    so_lan = n + 1
    for i in range(so_lan):
        sin = ((-1)**i)*((x**(2*i))/(giai_thua(2*i)))
        tong = tong + sin
    return tong

def approx_sinh(x, n):
    tong = 0
    so_lan = n + 1
    for i in range(so_lan):
        sin = ((x**(2*i+1))/(giai_thua(2*i+1)))
        tong = tong + sin
    return tong

def approx_cosh(x, n):
    tong = 0
    so_lan = n + 1
    for i in range(so_lan):
        sin = ((x**(2*i))/(giai_thua(2*i)))
        tong = tong + sin
    return tong