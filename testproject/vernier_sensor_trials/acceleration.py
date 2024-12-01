# Importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    dt= np.array([
    [1.2, -0.002],
    [1.25, -0.002],
    [1.3, 0.005],
    [1.35, 0.013],
    [1.4, 0.021],
    [1.5, 0.036],
    [1.55, 0.043],
    [1.6, 0.051],
    [1.65, 0.058],
    [1.7, 0.065],
    [1.75,	0.073],
    [1.8,	0.08],
    [1.85,	0.087],
    [1.9,	0.087],
    [1.95, .101],
    [2, 0.109],
    [2.05, 0.118],
    [2.1, 0.125],
    [2.15, 0.132],
    [2.2, 0.138],
    [2.25, 0.146],
    [2.3, 0.153],
    [2.35, 0.159],
    [2.4,	0.166],
    [2.45,	0.173],
    [2.5,	0.18],
    [2.55,	0.186],
    [2.6,	0.193],
    [2.65,	0.2],
    [2.7,	0.206],
    [2.75,	0.212],
    [2.8,	0.219],
    [2.85,	0.225],
    [2.9,	0.232],
    [2.95,	0.237],
    [3,	0.244],
    [3.05,	0.25],
    [3.1,	0.256],
    [3.15,	0.262],
    [3.2,	0.268],
    [3.25,	0.274],
    [3.3,	0.28],
    [3.35,	0.286],
    [3.4,	0.291],
    [3.45,	0.297],
    [3.5,	0.303],
    [3.55,	0.309],
    [3.6,	0.314],
    [3.65,	0.32],
    [3.7,	0.326],
    [3.75,	0.331],
    [3.8,	0.336],
    [3.85,	0.342],
    [3.9,	0.347],
    [3.95,	0.353],
    [4,	0.358],
    [4.05,	0.363],
    [4.1,	0.368],
    [4.15,	0.373],
    [4.2,0.378],
    [4.25,	0.383],
    [4.3,	0.388],
    [4.35,	0.393],
    [4.4,	0.398],
    [4.45,	0.408],
    [4.5,	0.413],
    [4.55,	0.417],
    [4.6,	0.422],
    [4.65,	0.426],
    [4.7,	0.431],
    [4.75,	0.435],
    [4.8,	0.439],
    [4.85,	0.443],
    [4.9,	0.448],
    [4.95,	0.448],
    [5,	0.451],
    ])

   # Generate data from array
    x = dt[:, 0]
    y = dt[:, 1]

    # Fit a line of best fit
    # coefficients = np.polyfit(np.log(x), y, 1)
    # poly = np.poly1d(coefficients)

    # Scatter plot with logarithmic axes
    # plt.scatter(x, y, label='Data')

    # # Line of best fit
    # plt.plot(x, poly(np.log(x)), color='blue', label='Line of Best Fit')

    # # Logarithmic axes
    # plt.xscale('log')
    # plt.yscale('log')
    
    velocity = np.gradient(y, x)
    acceleration = np.gradient(velocity, x)

    plt.figure(figsize=(10,6))
    plt.plot(x, velocity, label='Acceleration Function', color='blue')
    plt.title('Acceleration Function a(t)')

    # Labels and title
    plt.xlabel('Time in Seconds')
    plt.ylabel('a(t) In M/S^2')
    plt.title('Acceleration Function Chart')

    # Legend
    plt.legend()

    # Display the plot
    plt.show()


    page.appbar = ft.AppBar(
        title= ft.Text('Vernier Cart Day 1: Acceleration Graph', color=ft.colors.WHITE),
        bgcolor= ft.colors.BLUE
    )
    page.theme_mode = 'light'

    page.add(MatplotlibChart(plt, expand=True))

ft.app(main, view=ft.AppView.WEB_BROWSER)