x = int(input("Nhập số x: "))
is_prime = x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
print(f"{x} là số nguyên tố: {is_prime}")