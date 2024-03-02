message = input ('Eute a message')
Key = int(input ('Enter a Key:'))
index = 0
ms= " "
while (index<len (message)):
       letter = message [index]
       ms = ms+ chr (ord (letter) + Key)
       index = index+1
print ("'incrypted message in: ",ms)
