from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

dice = []
dice_num = int(input("Number of dice: "))
dice_sides = int(input("Number of dice sides: "))
roll_num = int(input("Number of rolls: "))

for die in range(dice_num):
    die = Die(dice_sides)
    dice.append(die)

results = []
#Rolling the dice and saving results
for roll in range(roll_num):
    result = 0
    for die in dice:
        result += die.roll()
    results.append(result)



#Analyzing results
frequencies = []

max_result = 0
for die in dice:
    max_result += die.num_sides

for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualization of results
x_values = list(range(1, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title' : 'Result', 'dtick' : 1}
y_axis_config = {'title' : 'Frequency of values'}
my_layout = Layout(title='Result of rolling {} dice D{} {} times'.format(dice_num, dice_sides, roll_num), xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename='die_visual.html')

