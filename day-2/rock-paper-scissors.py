stratGuide = open("input.txt", "r");

def values(x, y):
    if x == 'A':
        x = 1;
    elif x == 'B':
        x = 2;
    elif x == 'C':
        x = 3;
    if y == 'X':
        y = 1;
    elif y == 'Y':
        y = 2;
    elif y == 'Z':
        y = 3;
    atk = x;
    defs = y;
    return atk, defs;

def struct(x, y):
    roll = x - y;
    return roll;

roundScores = [];

roundScoresRev = [];

for rounds in stratGuide:
    opp = rounds[0];
    counter = rounds[2];
    atk, defs = values(opp, counter);
    if atk == defs:
        #draw
        roundScores.append(defs + 3);
    elif struct(atk, defs) == 2 or struct(atk, defs) == -1:
        #win
        roundScores.append(defs + 6);
    else:
        #loss
        roundScores.append(defs + 0);


print(sum(roundScores));

#Part 2

for rounds in stratGuide:
    opp = rounds[0];
    counter = rounds[2];
    if counter == 'X':
        if opp == 'A':
            counter = 'Z';
        elif opp == 'B':
            counter = ;
        else:
            counter = ;
    elif counter == 'Y';

    elif counter == 'Z';
