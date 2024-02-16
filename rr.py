
Number_Of_Quizzes = int(input("Enter number of quizzes: "))
My_score = []

while len(My_score) < Number_Of_Quizzes:
    Quiz_Score = input("Enter score for quiz {i}: ")

    My_score.append(Quiz_Score)
print(My_score)
