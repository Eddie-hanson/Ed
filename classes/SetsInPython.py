# Set In Python
students = [{"Name": "Edward", "House": "Kanda"}, {"Name": "Michael", "House": "Nima"}, {"Name": "Samuel", "House": "Kasoa"}, {
    "Name": "Jacob", "House": "Osu"}, {"Name": "Nana Yaw", "House": "Connecticut"}, {"Name": "Christian", "House": "New York"}, {"Name": "Jude", "House": "California"}, {"Name": "David", "House": "Geneva"}]

# houses = []

# for student in students:
#     if student["House"] not in houses:
#         houses.append(student["House"])
houses = set()
for student in students:
    if student["House"] not in students:
        houses.add(student["House"])


for house in sorted(houses):
    print(house)
