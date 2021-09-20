import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff

count = []
dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    #count.append(i)
#fig = px.bar(x = dice_result, y = count)
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_deviation = statistics.stdev(dice_result)
#fig = ff.create_distplot([dice_result], ["Result"])
#fig.show()
print("Mean is: " + str(mean))
print("Median is: " + str(median))
print("Mode is: " + str(mode))
print("Standard Deviation" +str(std_deviation))
#fig = ff.create_distplot([dice_result],["Result"], show_hist = False)
#fig.show()
