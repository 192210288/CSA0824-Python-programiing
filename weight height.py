weight=float(input("enter a weight"))
height=float(input("enter a height"))
BMI=weight/height**2
if(BMI<18.5):
    print("underweight")
elif(18.15<=BMI<25):
    print("normal weight")
else:
    print("overweight")
