"""
Exercise 6: Student Score Dictionary
Student: Likhita
Day: 2
"""

# input values
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# calculations
# 1
for student, score in student_scores.items():
  print(f"{student}: {score}")

# 2
atleast_60 = { student: score for student, score in student_scores.items() if score >= 60 }

# 3
top_student = max(student_scores, key=student_scores.get)
highest_score = max(student_scores.values())

# 4
average_score = sum(student_scores.values()) / len(student_scores)

# output
print(f"students who scored at least 60: {atleast_60}")
print(f"top student: {top_student}: {highest_score}")
print(f"averate score: {average_score:.2f}")
