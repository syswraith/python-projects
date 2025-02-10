import time
attempt = 0
n = int(input("Enter number: "))
time.sleep(0.7)
print(f"Generating Collatz conjecture for {n}")
while n != 1:
    if n % 2 != 0:
        n = n * 3 + 1
        attempt += 1
        time.sleep(0.7)
        print(int(n))
    else:
        n /= 2
        attempt += 1
        time.sleep(0.7)
        print(int(n))
time.sleep(3)
print(f"Attempts taken to reach loop at 1: {attempt}")
time.sleep(0.7)
