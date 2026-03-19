# ======================
# Control flow
# ======================


def grade_classifier(grade):
    if grade >= 90:
        return "Distinction"
    elif 60 <= grade <= 89:
        return "Pass"
    else:
        return "Fail"


print(grade_classifier(91))
print(grade_classifier(82))
print(grade_classifier(78))
print(grade_classifier(60))
print(grade_classifier(40))


scores = [45, 72, 91, 60, 38,85]

for score in scores:
    print(f"Result: {grade_classifier(score)}")
