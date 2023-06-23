# Create a function finalGrade, which calculates the final grade of a student 
# depending on two parameters: a grade for the exam and a number of completed projects.

# This function should take two arguments: exam - grade for exam (from 0 to 100); 
# projects - number of completed projects (from 0 and above);

# This function should return a number (final grade). There are four types of final grades:

# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

# which calculates the final grade of a student
def finalGrade(exam_grade, projects_completed):
    if exam_grade > 90 and projects_completed > 10: return 100
    elif exam_grade > 75 and projects_completed >= 5: return 90
    elif exam_grade > 50 and projects_completed >= 2: return 75
    else: return 0

print("The final grade is:", finalGrade(90,1))