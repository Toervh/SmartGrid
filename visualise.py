import csv
from code.classes.battery import Battery
from code.classes.house import House
from code.classes.district import District
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

output_file("plot.html")

#plot the points 
p = figure(title="Power Grid", x_axis_label='x', y_axis_label='y')
p.square(x_battery_list, y_battery_list, size=20, color="blue", alpha=0.5)
p.circle(x_house_list, y_house_list, size=10, color="red", alpha=0.5)

#plot lines between batteries and houses
battery_counter = 0
house_counter = 0

for battery in batteries:
    for house in houses:
        p.step([battery_x[battery_counter], house_x[house_counter]], [battery_y[battery_counter], house_y[house_counter]], line_width=1)
        house_counter+=1
    battery_counter+=1
    
#print results
show(p)



