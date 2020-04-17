students = {'Chang': {'Math': 90, 'Chinese': 85, 'English': 60},
            'Tang': {'Math': 85, 'Chinese': 70, 'English': 92},
            'Chen': {'Math': 90, 'Chinese': 93, 'English': 95}}

for student in students:
    # students[student].setdefault('total', 0)
    total = 0

    for grade in students[student]:
        total = total + students[student][grade]

    students[student].setdefault('total', total)

    # print(students[student][grade])

print(students)
