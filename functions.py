"""function to multiply two numbers"""            

# pre-defined

def mul(a,b):
    return ( a * b )

result = mul(5,7)
print(f"The result of multiplying both numbers is:{result}")


# user input

def mul(a,b):
    return ( a * b )


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

result = mul(num1 , num2)
print(f"The result of multiplying both numbers is:{result}")



""""function to check if a number is even or odd"""

def check_even_odd(num):

    if num % 2 == 0:
        print("Entered Number is Even.")

    else:
        print("Entered Number is Odd.")

result = int(input("Enter Number to check Even or Odd: "))
check_even_odd(result)

