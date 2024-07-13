e=[8,10,15,12,45,65,23,254,545,2313,132,13];s=1
while s:
    s=0 
    for i in range(len(e)-1):
        if e[i]>e[i+1]:s=1;e[i],e[i+1]=e[i+1],e[i];print(e)
