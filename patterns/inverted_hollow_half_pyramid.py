input = int(input("> "))
for x in range(input, 0, -1):
    if x==1 or x==input:
        print("*" * x)
    else:
        print("*" + " " * (x - 2) + "*")

