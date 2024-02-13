

f=open("world_cup_matches.csv")
rows=f.readlines()

table=[]
for row in rows[1:]:
    table.append(dict(zip(rows[0].strip('\n').replace(' ', '').split(','), row.strip('\n').replace(' ', '').split(','))))

def winners():
    winners=[]
    for row in table:
        if int(row["AwayGoals"])>int(row["HomeGoals"]):
            winners.append(row["AwayTeam"])
        else:
            winners.append(row["HomeTeam"])
    return winners

def wins_per_country(country):
    return winners().count(country)

def most_wins_v1():
    winners_list=winners()
    wins={}
    for winner in winners_list:
        wins.update({winners_list.count(winner):winner})
    return wins[max(wins)]

def most_wins_v2():
    country_scores={}
    for winner in winners():
        country_scores.update({wins_per_country(winner):winner})
    return country_scores[max(country_scores)]

def biggest_spread():
    biggest=0
    home=()
    away=()
    for row in table[:20]:
        spread=abs(int(row["AwayGoals"])-int(row["HomeGoals"]))
        if spread>biggest:
            biggest=spread
            home=row["HomeTeam"], row["HomeGoals"]
            away=row["AwayTeam"], row["AwayGoals"]
    return biggest, home, away

def wins_in_year(year):
    winners=[]
    for row in table:
        if int(row["Year"])==year:
            if int(row["AwayGoals"])>int(row["HomeGoals"]):
                winners.append(row["AwayTeam"])
            else:
                winners.append(row["HomeTeam"])
    return len(winners)

def year_most_wins():
    years=[]
    for row in table:
        years.append(int(row["Year"]))
    wins={}
    for year in years:
        wins.update({wins_in_year(year):year})
    return wins[max(wins)]

print(winners())
print(wins_per_country("England"))
print(wins_per_country("Spain"))
print(most_wins_v1())
print(most_wins_v2())
print(biggest_spread())
print(wins_in_year(1990))
print(year_most_wins(), wins_in_year(year_most_wins()))