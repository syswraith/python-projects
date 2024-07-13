example=[8,10,15,12,45,65,23,254,545,2313,132,13];swap=True
while swap:
    swap=False 
    for i in range(len(example)-1):
        if example[i]>example[i+1]:swap=True;example[i],example[i+1]=example[i+1],example[i];print(example)
