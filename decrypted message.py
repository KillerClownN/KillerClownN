decrypt = input ('Enter encrypted message')
Key = int(input ('Enter a Key:'))
index = 0
ms= " "
while (index<len (decrypt)):
       letter = decrypt [index]
       ms = ms+ chr (ord (letter) - Key)
       index = index+1
print ("'decrypted message is: ",ms)
