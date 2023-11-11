from math import gcd

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

ucln = gcd(a, b)
print(f"UCLN của {a} và {b} là: {ucln}")