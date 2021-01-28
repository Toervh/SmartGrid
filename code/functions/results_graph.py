import matplotlib.pyplot as plt
from pprint import pprint

def plot_results(results):



    # line 1 points
    x = list(range(len(results)))
    y = results

    # plotting the line 1 points
    plt.plot(x, y, label="line 1")

    # naming the x axis
    plt.xlabel('Tries')
    # naming the y axis
    plt.ylabel('Result')
    # giving a title to my graph
    plt.title('Results Graph')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    return plt.show()