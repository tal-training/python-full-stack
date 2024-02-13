student1={"Name":"Tal", "Phone":"052-111111", 
"Email":"tal@tal.com"}

student1["Name"]
student1["Phone"]
student1["Email"]

student2={"Name":"Gal", "Phone":"053-222222", "Email":"gal@gal.com"}

student2["Name"]
student2["Phone"]
student2["Email"]

students=[student1, student2]

students[0]["Name"]
students[0]["Phone"]
students[0]["Email"]

# print all emails in students table

for student in students:
    if student["Name"]=="Tal":
        print(student["Email"])

students={1:student1, 2:student2}

students={"tal":student1, "gal":student2}

students={student1["Name"]:student1, student2["Name"]:student2}
