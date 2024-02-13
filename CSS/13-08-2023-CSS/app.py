

with open("grades.csv") as f:
    lines=f.readlines()
    
html=""

for line in lines:
    html+=f"<div>{line.split(',')[0]}</div><div>{grade}</div>"
       

with open("grades.html", 'w') as f:
    f.write(html)



