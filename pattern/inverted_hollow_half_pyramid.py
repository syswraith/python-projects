input = int(input("> "))
for x in range(input, 1, -1):
    if x == 1 or x==input:
        print("*" * x)
    else:
        print("*" + " " * (x - 2) + "*")

