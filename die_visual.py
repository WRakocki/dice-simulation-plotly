from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die = Die()

results = []
#Rolling the dice and saving results
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

#Analyzing results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualization of results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {'title' : 'Frequency of values'}
my_layout = Layout(title='Result of rolling the dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename='d6.html')

