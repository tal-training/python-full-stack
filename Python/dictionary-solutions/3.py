# math homework

exercises={
    "1+1":"2",
    "2X2":"4",
    "3+2":"5",
    "5+4":"9",
    "5+6":"11",
    "2X6":"12",
    "6/2":"3",
    "12/3":"4",
    "12*2":"24",
    "100/2":"50"
}

score=0

for exercise in exercises:
    answer=input(f"{exercise}: ")
    if exercises[exercise]==answer:
        print("Correct!")
        score+=1
    else:
        print("Wrong answer, the correct answer is", exercises[exercise])

print("Your score is", score)