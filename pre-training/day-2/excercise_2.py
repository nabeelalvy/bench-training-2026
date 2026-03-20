students = [
    {"name": "Nabeel", "scores": [86, 94, 75, 90, 80], "subject": "CompSci"},
    {"name": "Sameer", "scores": [70, 69, 47, 65, 72], "subject": "Math"},
    {"name": "Bissam", "scores": [50, 60, 40, 60, 65], "subject": "History"},
    {"name": "Anas",   "scores": [55, 59, 89, 39, 97], "subject": "Physics"},
    {"name": "Sami",   "scores": [50, 85, 89, 80, 45], "subject": "Arts"},
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def class_topper(students):
    return max(students, key=lambda x: calculate_average(x["scores"]))

topper = class_topper(students)
sorted_students = sorted(students, key=lambda std: calculate_average(std["scores"]), reverse=True)

print(f"{'Name':<6} {'Subject':<7} {'Average':<8} {'Grade':<5} {''}")
print("-" * 45)

for student in sorted_students:
    average = calculate_average(student["scores"])
    grade = get_grade(average)
    tag = "*** TOP ***" if student["name"] == topper["name"] else ""
    print(f"{student['name']:<6} {student['subject']:<8} {average:<8} {grade:<5} {tag}")