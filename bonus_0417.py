students = {'Chang': {'Math': 90, 'Chinese': 85, 'English': 60},
            'Tang': {'Math': 85, 'Chinese': 70, 'English': 92},
            'Chen': {'Math': 90, 'Chinese': 93, 'English': 95}}

new = {}

for student in students:
    for grade in students[student]:
        new.setdefault(grade, {})
        new[grade].setdefault(student, students[student][grade])

print(new)
