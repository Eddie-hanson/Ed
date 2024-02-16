class Student:
    def __init__(self, name, house, ):

        self.name = name
        self.house = house

        # Getter in defining a getter you use '@property' above the function
    @property
    def house(self):
        return self._house

    # Setter in defining a setter use @ <Name of the setter function>.setter
    @house.setter
    def house(self, house):
        if house not in ["Kanda", "Osu", "Labadi", "Teshie", "Tse-Addo", "Legon",]:
            raise ValueError("Invalid Location")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name!!")
        self._name = name

    def __str__(self):
        return (f"{self.name}  lives at {self.house}")


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Enter your name: ")

    house = input("Where do you live: ")

    return Student(name, house, )


if __name__ == "__main__":
    main()
