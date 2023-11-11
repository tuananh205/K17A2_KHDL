import math

a = float(input("Nhập chiều dài cạnh a: "))
b = float(input("Nhập chiều dài cạnh b: "))
c = float(input("Nhập chiều dài cạnh c: "))

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Diện tích tam giác là: {area}")