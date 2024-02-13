import statistics

f=open("Salary_Data.csv")
rows=f.readlines()

table=[]
keys=rows[0].strip('\n').split(',')

for row in rows[1:]:
    clean_row=row.strip('\n').split(',')
    # כאן מוודאים שאין ערכים ריקים בשורה
    if '' not in clean_row:
        table.append(dict(zip(keys, clean_row )))

def max_salary():
    salaries=[]
    for row in table:
        salaries.append(int(row["Salary"]))
    return max(salaries)

def max_jobs():
    jobs=[]
    highest_salary=max_salary()
    for row in table:
        if int(row["Salary"])==highest_salary:
            jobs.append(row["Job Title"])
    return jobs

def average_age():
    ages=[]
    for row in table:
        ages.append(int(row["Age"]))
    return round(statistics.mean(ages), 2)

def average_salary_men():
    ages=[]
    for row in table:
        if row["Gender"]=="Male":
            ages.append(int(row["Salary"]))
    return round(statistics.mean(ages), 2)

def average_salary_women():
    ages=[]
    for row in table:
        if row["Gender"]=="Female":
            ages.append(int(row["Salary"]))
    return round(statistics.mean(ages), 2)

def highest_salary_ages():
    ages=[]
    highest_salary=max_salary()
    for row in table:
        if int(row["Salary"])==highest_salary:
            ages.append(row["Age"])
    return ages

def who_makes_more():
    if average_salary_men()>average_salary_women():
        return "Men"
    else:
        return "Women"
    
def gender_salary_difference():
    return round(abs(average_salary_men()-average_salary_women()),2)

def count_job_titles():
    titles=[]
    for row in table:
        titles.append(row["Job Title"])
    return len(set(titles))

def average_experience_developer():
    experiences=[]
    for row in table:
        if row["Job Title"].find("Developer")>-1:
            experiences.append(int(row["Years of Experience"]))
    return round(statistics.mean(experiences),2)

print("Highest salary:", max_salary())
print("Highest jobs:", max_jobs())
print("Average age:", average_age())
print("Highest paying ages:", highest_salary_ages())
print("Highest paying gender:", who_makes_more(), "\nDifference", gender_salary_difference())
print("Number of job titles:", count_job_titles())
print("Average developer years experience:", average_experience_developer())


