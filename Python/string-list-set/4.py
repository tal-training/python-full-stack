hotels=[["hilton",120], ["sheraton",220], ["isrotel",330]]

header="""
Select a vacation:
Hotel       Price per night
"""

print(header, end="")

for hotel in hotels:
    print(f"{hotel[0]}      {hotel[1]}")

