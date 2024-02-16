def my_func(x):
    if x == 0:
        return 1

    else:
        return (x*my_func(x-1))


Ask_user = int(input("Enter a number: "))
if Ask_user < 0:

    print("Enter a positive number")


else:
    result = my_func(Ask_user)
    print(f"The factorial of {Ask_user} is {result}")
