import numpy as np
import matplotlib.pyplot as plt


import flet as ft
from flet.matplotlib_chart import MatplotlibChart

# CONSTANT NO TOUCHY
g = 9.81  # acceleration due to gravity

# [angle (degrees), time of flight (s), horizontal distance (m), max height (m)]
trials_dt = [
    [60, 0.85, 1.82, 0.69],  # trial one
    [70, 0.96, 1.27, 0.66],  # trial two
    [80, 0.98, 0.58, 0.56]   # trial three
]

#I DONT KNOW WHY THESE WOWRK

def calculate_trajectory(theta, time_of_flight):

    # FROM DEG TO RADIANS
    theta_rad = np.radians(theta)
    
    # INIT VELOCITY
    v_0 = 2 * np.sqrt((g * time_of_flight * time_of_flight) / (2 * np.sin(theta_rad) * np.cos(theta_rad)))
    t = np.linspace(0, time_of_flight, 100)
    
    # x and y coordinate horizontal and vertical position
    x = v_0 * np.cos(theta_rad) * t
    y = v_0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    
    return x, y


plt.figure(figsize=(10, 6))


for trial in trials_dt:
    theta = trial[0]  # Launch angle
    time_of_flight = trial[1]  # Time of flight
    

    x, y = calculate_trajectory(theta, time_of_flight)
    
    # Plot the trajectory
    plt.plot(x, y, label=f"θ = {theta}°")

# Add labels, title, and legend
plt.title("Projectile Trajectories for Different Launch Angles")
plt.xlabel("Horizontal Distance (meters)")
plt.ylabel("Vertical Distance (meters)")
plt.legend(title="Launch Angles")
plt.grid(True)

# Loads the GUI
def main(page: ft.Page):

    g = 9.81  # acceleration due to gravity

    # Data from trials: [angle (degrees), time of flight (s), horizontal distance (m), max height (m)]
    trials_dt = [
        [60, 0.85, 1.82, 0.69],  # trial one
        [70, 0.96, 1.27, 0.66],  # trial two
        [80, 0.98, 0.58, 0.56]   # trial three
    ]

    #I DONT KNOW WHY THESE WOWRK

    def calculate_trajectory(theta, time_of_flight):

        # FROM DEG TO RADIANS
        theta_rad = np.radians(theta)
        
        # INIT VELOCITY
        v_0 = 2 * np.sqrt((g * time_of_flight * time_of_flight) / (2 * np.sin(theta_rad) * np.cos(theta_rad)))
        t = np.linspace(0, time_of_flight, 100)
        
        # x and y coordinate horizontal and vertical position
        x = v_0 * np.cos(theta_rad) * t
        y = v_0 * np.sin(theta_rad) * t - 0.5 * g * t**2
        
        return x, y

    #loads figure
    plt.figure(figsize=(10, 6))

    #load graph
    for trial in trials_dt:
        theta = trial[0] 
        time_of_flight = trial[1] 
        
        
        x, y = calculate_trajectory(theta, time_of_flight)
        
        
        plt.plot(x, y, label=f"θ = {theta}°")

    plt.title("Projectile Trajectories for Different Launch Angles")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.legend(title="Launch Angles")
    plt.grid(True)

    page.appbar = ft.AppBar(
        title= ft.Text('Projectile Launching Day 4: Position VS Time Graph', color=ft.colors.WHITE),
        bgcolor= ft.colors.BLUE
    )
    page.theme_mode = 'light'

    page.add(MatplotlibChart(plt, expand=True))

ft.app(main, view=ft.AppView.WEB_BROWSER)