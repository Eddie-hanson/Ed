#      Question:
# Write a Python program to calculate the factorial of a given non-negative integer using a function. The factorial of a number
# �
# n is the product of all positive integers less than or equal to
# �
# n. The program should take user input for the integer and then output the calculated factorial.

# Requirements:

# Use a function named calculate_factorial to perform the factorial calculation.
# Handle the case where the user enters a negative integer gracefully, displaying an error message and prompting for input again.
# This question will test your understanding of how to structure a program using functions, handle user input, and implement a basic mathematical calculation.
# Feel free to attempt it, and I can provide guidance or the solution if needed!


# def caculate_factorial(number):
#     if number == 0 or number == 1:
#         return 1

#     else:
#         return number*caculate_factorial(number - 1)


# user_input = int(input("Enter a positive number: "))

# if user_input < 0:
#     print("Entered a negative number. ")

# else:
#     result = caculate_factorial(user_input)

#     print(f"The factoria of {user_input} is {result}  ")

#                                              2

# Write a Python function to check if a given number is even or odd. The program should take user input,
# call the function, and print whether the number is even or odd.

# def even_odd(number):
#     if number % 2 == 0:
#         return ("You number is even")
#     else:
#         return ("Your number is odd")


# while True:
#     user_input = int(input("Enter a number: "))
#     result = even_odd(user_input)

#     print(result)
# # as if user wants to continue
#     print("Enter Yes to continue and No to Exit.")
#     AskUser = input("Do you want to continue:")

#     Y = "Yes"
#     N = "No"

#     if AskUser == Y:
#         continue
#     else:
#         if AskUser == N:
#             break
