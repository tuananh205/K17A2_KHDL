from math import lcm

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

bcln = lcm(a, b)
print(f"BCLN của {a} và {b} là: {bcln}")