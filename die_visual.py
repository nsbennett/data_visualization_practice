import plotly.express as px

from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


# results_dict = {}
# for x, y in enumerate(frequencies):
#     results_dict[f"{x + 1}"] = y



fig = px.bar(x=poss_results, y=frequencies)
fig.show()