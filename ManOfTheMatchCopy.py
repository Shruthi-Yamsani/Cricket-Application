#1.Code to compute points earned by players 
BatPeople = { 'p1': {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}, 
         'p2': {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}}
BowlPeople ={ 'p3': {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1},
         'p4': {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0},
         'p5': {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}}

#batting people function
def battingResults(name, runs, strikeRate, fours, sixes):
    points = runs/2
    if runs > 50:
        points = points + 5
        if runs >= 100:
            points = points + 10
    if strikeRate >= 80 and strikeRate <= 100:
        points = points + 2
    if strikeRate > 100:
        points = points + 4
    if fours > 1:
        fours = fours * 1
    if sixes > 1:
        sixes = sixes * 2
    batScore = points + fours + sixes
    newDict = {'name' : name, 'batScore' : int(batScore)}
    print(newDict)

#bowling people function
def bowlingResults(name, runScore1, wickets):
    economyPoints = 0
    overs = 10
    economyRate = runScore1/overs
    wicketPoints = wickets * 10
    wicketPoints1 = 0
    if wickets >= 1 and wickets < 3:
        wicketPoints1 = wicketPoints + 0
    elif wickets == 3:
        wicketPoints1 = wicketPoints + 5
    elif wickets >= 5:
        wicketPoints1 = wicketPoints + 5 + 10       
    if economyRate >= 3.5 and economyRate <= 4.5:
        economyPoints = 4
    elif economyRate >= 2 and economyRate <= 3.5:
        economyPoints = 7
    elif economyRate < 2:
        economyPoints = 10
    bowlscore = wicketPoints1 + economyPoints
    newDict = {'name' : name , 'bowlscore' : bowlscore}
    print(newDict)

for i in BatPeople.keys():
    battingResults(BatPeople[i].get('name'), BatPeople[i].get('runs'), BatPeople[i].get('balls'), BatPeople[i].get('4'), BatPeople[i].get('6'))


for i in BowlPeople.keys():
    bowlingResults(BowlPeople[i].get('name'), BowlPeople[i].get('runs'), BowlPeople[i].get('wkts'))

#2. 
