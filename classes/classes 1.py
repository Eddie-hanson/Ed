# Syntax
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

class Register:
    def __init__(self, name, timeIn, signOutTime):
        self.name = name
        self.timeIn = timeIn
        self.signOutTime = signOutTime

    def __str__(self):
        return f" Client name: {edward.name}\n Reported at: {edward.timeIn} \n Signed out at {edward.signOutTime}"


edward = Register(input("Enter Name: "), input(
    "Enter time reported: "), input("Time signed out: "))
print(edward)
