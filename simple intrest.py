p=int(input("enter a number"))
n=int(input("enter the number of years"))
sc=input("male/female")
if sc=='y' and g=='m':
    print("sl=",(p*n*15)/100)
elif sc=='y' and g=='f':
    print("sl=",(p*n*15)/100)
else:
    print("sl=",(p*n*10)/100)
          
