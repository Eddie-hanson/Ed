
# from string import ascii_letters
# from string import digits
from string import ascii_letters, digits, punctuation

# Generating a four digit number--> from string import digits
# for i in digits:
#     for j in digits:
#         for k in digits:
#             for l in digits:
#                 print(i, j, k, l)

# Generating a four letter combination-->  #from string import digits

# for i in ascii_letters:
#     for j in ascii_letters:
#         for k in ascii_letters:
#             for l in ascii_letters:
#                 print(i, j, k, l)

# Generating a four digit code from a combination of numbers, letters, and punctuations -->from string import ascii_letters, digits, punctuation

for i in ascii_letters+digits + punctuation:
    for j in ascii_letters + digits+punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)
