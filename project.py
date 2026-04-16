marks=int(input("Enter the marks of 6 subjects:"))
perc=(marks/600)*100
print("Percentage is ",perc)
if(marks>=450):
    print("Grade A")
elif(marks>=350):
    print("Grade B")
else:
    print("Needs Improvment....:(")