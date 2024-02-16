course_name=input("enter your course name: ")
exam_score=int(input("Enter your exam score: "))
credit_hour=int(input("Enter credit hour: "))
if exam_score <=59:
    print(f"You had an F and a grade point of 0.0 in {course_name}")
elif exam_score <=69:
 print(f"You had a D and a grade point of 1 .0 in {course_name}")
elif exam_score <=79:
     print(f"You had a C and a grade point of 2.0 in {course_name}")
elif exam_score <=89:
    print(f"You had a B and a grade point of 4.0 in {course_name}")
    
else:
  print(f"You had an A and a grade point of 4.0 in {course_name}")