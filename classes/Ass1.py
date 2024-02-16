class UG_Student:

    def __init__(self, Name, grades, ):
        self.Name = Name
        self.grades = grades
    My_score = []

    @classmethod
    def getScore(cls):
        Name = input("Enter your name:")
        cls.Number_Of_Quizzes = int(input("Enter Number of quizzes:"))
        cls.My_score = []
        while len(cls.My_score) < cls.Number_Of_Quizzes:
            cls.Quiz_Score = int(input("Enter result:"))
            cls.My_score.append(cls.Quiz_Score)
            return cls.Quiz_Score
        grades = cls.Quiz_Score
        return UG_Student(Name, grades)

    # def getName():

    #     Name = input("Enter your Name: ")

    #     return UG_Student(Name, grades)

    # def __str__(self):

    #     return f"{self.Name} your grades are {grades}"

    # My_score = []
    # Number_Of_Quizzes = int(input("Enter Number of quizzes:"))

    # @classmethod
    # def getScore(cls, My_score, Number_Of_Quizzes):
    #     while len(cls.My_score) < cls.Number_Of_Quizzes:
    #         Quiz_Score = input("Enter score for quiz {i}: ")
    #         cls.My_score.append(Quiz_Score)

    #         return UG_Student(cls.My_score)


def main():
    student = UG_Student.getScore()
    print(student)


if __name__ == "__main__":
    main()
