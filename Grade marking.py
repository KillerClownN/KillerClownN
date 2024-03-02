#wap to give grade for the given marks:m>=90:A, m>=80, m>=70:c, m>=60:d,
#m>=40:E, m<40:f
a=int(input("Enter marks of student:"))
if (a>=90):
    print("The student has obtained grade:A")
elif (a>=80):
    print("The student has obtained grade:B")
elif (a>=70):
    print("The student has obtained grade:C")
elif (a>=60):
    print("The student has obtained grade:D")
elif (a>=40):
    print("The student has obtained grade:E")
else:
    print("The student has obtained grade:F")

