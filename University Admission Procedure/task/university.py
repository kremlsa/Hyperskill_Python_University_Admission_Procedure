def find_applicant(x_, y_, n_, department_):
    for applicant_ in department_:
        if x_ == applicant_[0] and y_ == applicant_[1] and n_ == applicant_[3]:
            return True
    return False


def remove_applicants(department_, n_):
    temp = []
    for applicant in applicants:
        if not find_applicant(applicant[0], applicant[1], applicant[n_], department_):
            temp.append(applicant)
    return temp


def save_to_file(name_, department_):
    with open(name_ + ".txt ", "w", encoding='utf-8') as myfile:
        for student_ in department_:
            myfile.write("{} {} {}\n".format(student_[0], student_[1], student_[2]))


num_accepted = int(input())
applicants = []
physics = []
engineering = []
mathematics = []
biotech = []
chemistry = []
with open("applicants.txt ") as file:
    for line in file.readlines():
        applicants.append(line.split())

applicants = [[x, y, int(a), int(b), int(c), int(d), int(s), d1, d2, d3] for [x, y, a, b, c, d, s, d1, d2, d3] in applicants]

for n in range(7, 10):
    applicants.sort(key=lambda x: (x[0], x[1]))
    applicants.sort(reverse=True, key=lambda x: (max((x[2] + x[4]) / 2, x[6])))
    physics_ = [[x[0], x[1], max((x[2] + x[4]) / 2, x[6]), x[n]] for x in applicants if x[n] == "Physics"][:num_accepted]
    if len(physics) < num_accepted:
        for x in range(min(num_accepted - len(physics), len(physics_))):
            physics.append(physics_[x])
    applicants = remove_applicants(physics, n)

    applicants.sort(key=lambda x: (x[0], x[1]))
    applicants.sort(reverse=True, key=lambda x: (max((x[5] + x[4]) / 2, x[6])))
    engineering_ = [[x[0], x[1], max((x[5] + x[4]) / 2, x[6]), x[n]] for x in applicants if x[n] == "Engineering"][:num_accepted]
    if len(engineering) < num_accepted:
        for x in range(min(num_accepted - len(engineering), len(engineering_))):
            engineering.append(engineering_[x])
    applicants = remove_applicants(engineering, n)

    applicants.sort(key=lambda x: (x[0], x[1]))
    applicants.sort(reverse=True, key=lambda x: (max(x[4], x[6])))
    mathematics_ = [[x[0], x[1], max(x[4], x[6]), x[n]] for x in applicants if x[n] == "Mathematics"][:num_accepted]
    if len(mathematics) < num_accepted:
        for x in range(min(num_accepted - len(mathematics), len(mathematics_))):
            mathematics.append(mathematics_[x])
    applicants = remove_applicants(mathematics, n)

    applicants.sort(key=lambda x: (x[0], x[1]))
    applicants.sort(reverse=True, key=lambda x: (max(x[3], x[6])))
    chemistry_ = [[x[0], x[1], max(x[3], x[6]), x[n]] for x in applicants if x[n] == "Chemistry"][:num_accepted]
    if len(chemistry) < num_accepted:
        for x in range(min(num_accepted - len(chemistry), len(chemistry_))):
            chemistry.append(chemistry_[x])
    applicants = remove_applicants(chemistry, n)

    applicants.sort(key=lambda x: (x[0], x[1]))
    applicants.sort(reverse=True, key=lambda x: (max((x[3] + x[2]) / 2, x[6])))
    biotech_ = [[x[0], x[1], max((x[3] + x[2]) / 2, x[6]), x[n]] for x in applicants if x[n] == "Biotech"][:num_accepted]
    if len(biotech) < num_accepted:
        for x in range(min(num_accepted - len(biotech), len(biotech_))):
            biotech.append(biotech_[x])
    applicants = remove_applicants(biotech, n)

biotech.sort(key=lambda x: (x[0], x[1]))
biotech.sort(reverse=True, key=lambda x: (x[2]))
chemistry.sort(key=lambda x: (x[0], x[1]))
chemistry.sort(reverse=True, key=lambda x: (x[2]))
engineering.sort(key=lambda x: (x[0], x[1]))
engineering.sort(reverse=True, key=lambda x: (x[2]))
mathematics.sort(key=lambda x: (x[0], x[1]))
mathematics.sort(reverse=True, key=lambda x: (x[2]))
physics.sort(key=lambda x: (x[0], x[1]))
physics.sort(reverse=True, key=lambda x: (x[2]))

print("Biotech")
save_to_file("biotech", biotech)
for student in biotech:
    print(student[0], student[1], float(student[2]), sep=" ")
print()
print("Chemistry")
save_to_file("chemistry", chemistry)
for student in chemistry:
    print(student[0], student[1], float(student[2]), sep=" ")
print()
print("Engineering")
save_to_file("engineering", engineering)
for student in engineering:
    print(student[0], student[1], float(student[2]), sep=" ")
print()
print("Mathematics")
save_to_file("mathematics", mathematics)
for student in mathematics:
    print(student[0], student[1], float(student[2]), sep=" ")
print()
print("Physics")
save_to_file("physics", physics)
for student in physics:
    print(student[0], student[1], float(student[2]), sep=" ")
print()
