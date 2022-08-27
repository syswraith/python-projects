import random
import time

def porthack():
    print("generating random p...")
    time.sleep(3)
    tuplePorts = (21, 22, 23, 25, 53, 69, 80, 443, 3389, 5900, 8080)
    n = random.choice(tuplePorts)

    print(f"Random p: {n}")
    time.sleep(1)

    attempt = 0
    print("Attempting a crack... ")
    time.sleep(3)
    while n != 1:
        if n % 2 != 0:
            n = n * 3 + 1
            time.sleep(0.7)
            attempt += 1
            print(int(n))   
        else:
            n /= 2
            time.sleep(0.7)
            attempt += 1
            print(int(n))
    time.sleep(3)
    print(f"attempts taken: {attempt}")
    time.sleep(0.7)
    print("gotem")

