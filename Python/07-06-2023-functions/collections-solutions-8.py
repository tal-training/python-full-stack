import statistics

users=[
{"Name":"Tal", "Course":"Python", "Grade":95, "Email":"tal@tal.com"},
{"Name":"Shmuel", "Course":"HTML", "Grade":80, "Email":"shmuel@gmail.com"},
{"Name":"Zehava", "Course":"Javascript", "Grade":98, "Email":"zva@gmail.com"}
]

grades=[]

for user in users:
    grades.append(user["Grade"])

print(max(grades), min(grades))

print(statistics.mean(grades))