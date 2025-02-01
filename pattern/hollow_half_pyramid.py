input = int(input("> "))
for x in range(1,input + 1):
    if x == 1 or x==input:
        print("*" * x)
    else:
        print("*" + " " * (x - 2) + "*")

