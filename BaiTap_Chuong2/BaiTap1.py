import math

try:
    r = float(input("Moi ban nhap ban kinh hinh tron: "))
    cv = 2 * math.pi * r
    dt = r * 2
    print("chu vi =", cv)
    print("dt =", dt)
except:
    print("loi roi!")
