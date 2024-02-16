def calculate_gpa(score):
    if 90 <= score <= 100:
        return 4.0
    elif 80 <= score < 90:
        return 3.0
    elif 70 <= score < 80:
        return 2.0
    elif 60 <= score < 70:
        return 1.0
    else:
        return 0.0

def main():
    num_courses = int(input("Enter the number of courses: "))
    total_credit_hours = 0
    total_weighted_gpa = 0

    for i in range(num_courses):
        course_name = input("Enter course name: ")
        exam_score = float(input("Enter exam score (out of 100): "))
        credit_hours = int(input("Enter credit hours: "))

        grade = calculate_gpa(exam_score)
        weighted_gpa = grade * credit_hours

        total_weighted_gpa += weighted_gpa
        total_credit_hours += credit_hours

        print(f"Course: {course_name}")
        print(f"Exam Score: {exam_score}")
        print(f"Credit Hours: {credit_hours}")
        print(f"Grade: {grade:.1f}\n")

    if total_credit_hours > 0:
        final_gpa = total_weighted_gpa / total_credit_hours
        print(f"Calculated GPA: {final_gpa:.2f}")
    else:
        print("No courses were entered.")

    if course_name == "main":
