students = {'Chang': {'Math': 90, 'Chinese': 85, 'English': 60},
            'Tang': {'Math': 85, 'Chinese': 70, 'English': 92},
            'Chen': {'Math': 90, 'Chinese': 93, 'English': 95}}

pre = []
rank = []
index = 0

for student in students:
    # students[student].setdefault('total', 0)
    total = 0

    for grade in students[student]:
        total = total + students[student][grade]

    students[student].setdefault('total', total)
    pre.append(total)

    # print(students[student][grade])

for a in pre:
    base = len(pre)
    for b in pre:
        if a > b:
            base = base - 1
    rank.append(base)

for student in students:
    students[student].setdefault('rank', rank[index])
    index = index + 1

print(students)
