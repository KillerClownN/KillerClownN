s=input("Enter a string:")
ns=""
for i in range(len(s),0,-1):
    l=s[i-1]
    ns=ns+l
print("the reversed string is:",ns)
