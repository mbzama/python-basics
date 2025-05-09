num=input("Enter a number:")
if num.isdigit():
    num=int(num)
    print("Number is: ", num)

    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")

else:
    print("Please enter a valid number")
    exit()
