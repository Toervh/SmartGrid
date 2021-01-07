import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
import matplotlib.pyplot as plt


#Plotting the batteries and houses

#Creating an empty plot
x = range(60)
y = range(60)
fig = plt.figure()
ax1 = fig.add_subplot(111)

#Adding batteries
batteries = District.batteries
for battery in batteries:
    battery[0] = x
    battery[1] = y
    print(x, y)
    ax1.scatter(x, y, c="r", label='batteries')

#Adding houses
houses = District.houses
for house in houses:
    house[0] = x
    house[1] = y
    ax1.scatter(x, y, c="b", label='houses')

plt.show()