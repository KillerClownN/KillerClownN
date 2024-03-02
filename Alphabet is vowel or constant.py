#wap to check if the given alphabet is a vowel or consonant
a=input("Enter a alphabet:")
if (a.lower() in ("a" ,"e" ,"i" ,"o" ,"u")):
    print("The given alphabet is Vowel")
elif (a.upper() in ("A" ,"E" ,"I" ,"O" ,"U")):
    print ("The given numb er is a vowel")
else:
    print("The given alphabet is a consonant")
