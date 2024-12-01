# Importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

# Define the range for t
t = np.linspace(0, 10, 100)  # t ranges from 0 to 10 with 100 points

# Define the linear functions
y1 = 3.27 * t  # Function 1: y = 3.27t
y2 = 0.98 * t  # Function 2: y = 0.98t
y3 = 2.2 * t   # Function 3: y = 2.2t

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each function
plt.plot(t, y1, label="y = 3.27t", color="blue")
plt.plot(t, y2, label="y = 0.98t", color="green")
plt.plot(t, y3, label="y = 2.2t", color="red")

# Add labels, title, and legend
plt.title("Linear Functions")
plt.xlabel("Time")
plt.ylabel("y")
plt.legend()

# Show the plot
def main(page: ft.Page):
    t = np.linspace(0, 10, 100)  # t ranges from 0 to 10 with 100 points

    # Define the linear functions
    y1 = 3.27 * t  # Function 1: y = 3.27t
    y2 = 0.98 * t  # Function 2: y = 0.98t
    y3 = 2.2 * t   # Function 3: y = 2.2t

    # Gradients (derivatives) of the functions
    gradient1 = np.full_like(t, 3.27)  # Gradient of y1
    gradient2 = np.full_like(t, 0.98)  # Gradient of y2
    gradient3 = np.full_like(t, 2.2)   # Gradient of y3

    # Create a figure
    plt.figure(figsize=(10, 6))

    # Plot the gradients
    plt.plot(t, gradient1, label="Trial 1", color="blue", linestyle="--")
    plt.plot(t, gradient2, label="Trial 2", color="green", linestyle="--")
    plt.plot(t, gradient3, label="Trial 3", color="red", linestyle="--")

    # Add labels, title, and legend
    plt.title("Acceleration Graph (Gradiant of Velocity)")
    plt.xlabel("t")
    plt.ylabel("a(t)")
    plt.legend()
    plt.grid(True)

    #Builds the GUI
    page.appbar = ft.AppBar(
        title= ft.Text('Vernier Cart Day 3: Acceleration VS Time Graph', color=ft.colors.WHITE),
        bgcolor= ft.colors.BLUE
    )
    page.theme_mode = 'light'

    page.add(MatplotlibChart(plt, expand=True))

ft.app(main, view=ft.AppView.WEB_BROWSER)