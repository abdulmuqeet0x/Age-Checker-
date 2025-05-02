print("Hello! Welcome to Age Checker.")

age = float(input("Enter You'r Age: "))

if age <= 0:
    print("Invalid! Age Please Enter correct one.")

elif age > 0 and age < 18 :
    print("You are underage.")

elif age >= 18:
    print("You Are 18th or Above ")

else:
    print("something went wrong.")


