#wap to calculate the total salary taking input the basic salary:bs<=10k then hra will 20% and da 80%....bs<=20k hra=25% and da will 90%.....if bs>20k hra 30% da 95%
bs=int(input("Enter basic salary:"))
if (bs<=10000):
    hra=20/100*bs
    da=80/100*bs
    ts=bs+hra+da
    print("Total salary=",ts)
elif (bs<=20000):
    hra=25/100*bs
    da=90/100*bs
    ts=bs+hra+da
    print("Total salary=",ts)
else:
    hra=20/100*bs
    da=95/100*bs
    ts=bs+hra+da
    print("Total salary=",ts)
