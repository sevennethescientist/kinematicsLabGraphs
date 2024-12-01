# Importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

def main(page: ft.Page):
    
    # Constants
# Data for trials: [angle (degrees), time of flight (s), horizontal distance (m), max height (m)]
    trials_dt = [
        [60, 0.85, 1.82, 0.69],  # trial one
        [70, 0.96, 1.27, 0.66],  # trial two
        [80, 0.98, 0.58, 0.56]   # trial three
    ]

    # Extract time of flight and horizontal distance for each trial
    time_of_flight = [trial[1] for trial in trials_dt]
    horizontal_distance = [trial[2] for trial in trials_dt]

    # Create a figure
    plt.figure(figsize=(10, 6))

    # Plot position (horizontal distance) vs time for each trial
    for i, trial in enumerate(trials_dt):
        theta = trial[0]  # angle
        t_flight = trial[1]  # time of flight
        x_position = trial[2]  # horizontal distance
        label = f"θ = {theta}°"

        # For simplicity, plot a line connecting the start (0, 0) to the horizontal distance at the time of flight
        plt.plot([0, t_flight], [0, x_position], label=label)

    # Add labels, title, and legend
    plt.title("Position vs Time for Different Launch Angles")
    plt.xlabel("Time (seconds)")
    plt.ylabel("x(t) In Horizontal Distance (m)")
    plt.legend(title="Launch Angles")
    plt.grid(True)

    #Builds the GUI
    page.appbar = ft.AppBar(
        title= ft.Text('Projectile Launching Day 4: Position VS Time Graph', color=ft.colors.WHITE),
        bgcolor= ft.colors.BLUE
    )
    page.theme_mode = 'light'

    page.add(MatplotlibChart(plt, expand=True))

ft.app(main, view=ft.AppView.WEB_BROWSER)