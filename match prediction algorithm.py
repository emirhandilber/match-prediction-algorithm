print('''Welcome to match prediction algorithm.
Lets begin with first team  ''')
team1 = input('Type the team name : ')
print('You choose the team, lets continiue with match statics.')
victories1 = int(input('Type number of wins :'))
loses1 = int(input('Type number of loses : '))
goalscored1 = int(input('Type number of scored goal : '))
goalate1 = int(input('Type number of aten goal : '))
injured1 = int(input('Type injured players : '))
print('Lets choose second team : ')
team2 = input('Type the second team name : ')
print('You choose the team, lets continiue with match statics.')
victories2 = int(input('Type number of wins :'))
loses2 = int(input('Type number of loses : '))
goalscored2 = int(input('Type number of scored goal : '))
goalate2 = int(input('Type number of aten goal : '))
injured2 = int(input('Type injured players : '))
o11 = victories1 - loses1
o12 = (goalscored1 - goalate1)/3
o13 = injured1 * (-3)
o21 = victories2 - loses2
o22 = (goalscored2 - goalate2)/3
o23 = injured2 * (-3)
o1 = o11 + o12 + o13
o2 = o21 + o22 + o23
if o1 > o2:
    print(team1, ' has the chance to win')
elif o1 < o2:
    print(team2, ' has the chance to win')
