def average(numbers):
    total = 0
    for i in numbers:
        total = total + i

    for i in range(len(numbers)):
        return (total/len(numbers))


def largest_number(numbers):
    for i in numbers:
        largest_number = 0
        if i > largest_number:
            largest_number = i
        # print(largest_number)
    return largest_number


my_numbers = [1, 2, 3, 4, 5]


mean = average(my_numbers)
print(f"The mean is {mean}")


max_value = largest_number(my_numbers)
print(f"Then maximun value is {max_value}")
