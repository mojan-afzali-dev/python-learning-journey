weight=float(input("enter your weight in Kg: "))
hight= float(input("enter your hight in m: "))
BMI= weight / (hight**2)
print(BMI)
if BMI < 18.5:
    print("you are under-weight")
elif BMI <= 25 :
    print("you are a fit person")
else:
    print("you are over-weight")



