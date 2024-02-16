#normal_rate=10.00
#normal_working_hour=8
#overtime_rate=15.00
#my_working_hour=int(input("Enter the number of hour worked: "))
#salary= normal_rate*my_working_hour
#overtime_hours=my_working_hour-normal_working_hour
#overtime_salary=overtime_hours*overtime_rate

#if(my_working_hour <= normal_working_hour):
#   {print(salary)}

#else: 
 
# new_salary=overtime_salary+salary
# print (f"Your new salary is GhC {new_salary})



#age=int(input("Enter your age: ")) 
#if age>=18:
#    print("You can vote")
#else:
#    print("You are not eligible to vote")

#NESTED CONDITIONS
#x= 10
#y = 5
#if x>y:
#    print("x is greater than y")
#    if x > 15:
 #       print("x is greater than 15")
 #   else:
 #        print("x is less than y")
#else:
#    print("x is less than y")

username = "Mr. Hanson"
Password = "1234edward"
login_username=input("What is your username: ")
login_password=input("What is your password: ")

if login_username==username & login_password==Password:
    print(f"Welcome {username}")
    if login_username!=username :
        print("Incorrect Username")

    if login_username == username & login_password!=Password:
        print("Incorrect password")
    
    
else:
        print("This user does not exist")