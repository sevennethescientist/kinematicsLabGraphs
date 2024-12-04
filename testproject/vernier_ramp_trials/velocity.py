# Importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft
from flet.matplotlib_chart import MatplotlibChart


# Show the plot via FLET
def main(page: ft.Page):
    # Range for t
    t = np.linspace(0, 10, 100)  # t ranges from 0 to 10 with 100 points

    #line functions
    y1 = 3.27 * t  # Function 1: y = 3.27t
    y2 = 0.98 * t  # Function 2: y = 0.98t
    y3 = 2.2 * t   # Function 3: y = 2.2t


    plt.figure(figsize=(10, 6))


    plt.plot(t, y1, label="Trial One", color="blue")
    plt.plot(t, y2, label="Trial Two", color="green")
    plt.plot(t, y3, label="Trial Three", color="red")

    plt.title("Trial Comparison Speeed")
    plt.xlabel("Time in Seconds")
    plt.ylabel("v(t)")
    plt.legend()

    page.appbar = ft.AppBar(
        title= ft.Text('Vernier Cart Day 3: Velocity VS Time Graph', color=ft.colors.WHITE),
        bgcolor= ft.colors.BLUE
    )
    page.theme_mode = 'light'

    page.add(MatplotlibChart(plt, expand=True))

ft.app(main, view=ft.AppView.WEB_BROWSER)