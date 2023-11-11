import time

n = int(input("Input number: "))
print(*range(n, 0, -1), "Start!!!", sep='\n')
time.sleep(n) 