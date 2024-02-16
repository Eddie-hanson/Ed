# >- greater than, >= greater or equal to,  < -less than, <= less or equal to, == -equal to, != not equal to
# X = int(input("What is X ? "))
# Y = int(input("What is Y ? "))

# if X < Y:
#     print("X is less than Y")
# elif X > Y:
#     print("X is greater than Y")
# else:
#     print("X is equal to Y")

# OR
# if X < Y or X > Y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to Y")

#!=
# if X != Y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to Y")

# ==
# if X == Y:
#     print("X is equal to Y")
# else:
#     print(" X is not equal to Y")

# AND
# Score = int(input("Enter your score: "))

# if Score >= 90 and Score <= 100:
#     print("Grade: A")
# elif Score >= 80 and Score < 90:
#     print("Grade: B")
# elif Score >= 70 and Score < 80:
#     print("Grade: C")
# elif Score >= 60 and Score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# Achieving same results with less code
# if 90 <= Score <= 100:
#     print("Grade: A")
# elif 80 <= Score < 90:
#     print("Grade: B")
# elif 70 <= Score < 80:
#     print("Grade: C")
# elif 60 <= Score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# if Score >= 90:
#     if Score > 100:
#         print("Score cannot be greater than 100")
#     else:
#         print("Grade: A")
# elif Score >= 80:
#     print("Grade: B")
# elif Score >= 70:
#     print("Grade: C")
# elif Score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# The % operator
# 1
# X = int(input("What's X? "))

# if X % 2 == 0:
#     if X == 0 or 1:
#         print("X is not an even Number")
#     else:
#         print("X is even")
# else:
#     print("X is odd")

# def main():
#     X = int(input("Enter A number: "))
#     if Is_even(X):
#         print("The number is even ")
#     else:
#         print("Is odd")


# def Is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# 2
# def Is_even(n):
#     return True if n % 2 == 0 else False

# 3.
# def Is_even(n):
#     return n % 2 == 0


# if __name__ == "__main__":
#     main()

# Match similar to switch cases in other languages like JAVA and C++
# Normal way of doing it
Name = input("What is your name: ")
# if Name == "Nana":
#     print(f"{Name} lives at Nungua")
# elif Name == "Joseph":
#     print(f"{Name} lives at Kasoa")
# elif Name == "Edward":
#     print(f"{Name} lives at Kanda")
# elif Name == "Kwesi":
#     print(f"{Name} lives at Osu")
# elif Name == "Maggie":
#     print(f"{Name} lives at Tamale")
# elif Name == "Afia":
#     print(f"{Name} lives at Dzowulu")
# else:
#     print(f"The name {Name} does not exist in the Database")

# Using match case
match Name:
    case "Nana" | "Takie" | "Mamle":
        print(f"{Name} lives at Nungua")
    case "Joseph":
        print(f"{Name} lives at Kasoa")
    case "Edward":
        print(f"{Name} lives at Kanda")
    case "Kwesi":
        print(f"{Name} lives at Osu")
    case "Maggie":
        print(f"{Name} lives at Tamale")
    case "Afia":
        print(f"{Name} lives at Dzowulu")
    case _:
        # (case _) used for default statements or cases
        print(f"The name {Name} does not exist in the Database")
