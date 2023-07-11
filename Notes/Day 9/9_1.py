student_scores = {
  "Harry": 81,
  "Ron": 81,
  "Hermione": 100,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
    if student_scores[score] in range(91,101):
        student_grades[score] = 'Outstanding'
    elif student_scores[score] in range(81,91):
        student_grades[score] = 'Exceeds Exceptations'
    elif student_scores[score] in range(71,81):
        student_grades[score] = 'Acceptable'
    elif student_scores[score] <= 70:
        student_grades[score] = 'Fail'

print(student_grades)