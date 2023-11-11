n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
result = (x**2 + x + 1)**n + (x**2 - x + 1)**n
print(f"A = (x^2 + x + 1)^n + (x^2 - x + 1)^n = {result}")