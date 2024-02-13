import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Create figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)

# Create initial plot (empty)
line, = ax.plot([], [], 'o-', lw=2, color='white')  # Projectile motion trajectory in blue
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Projectile Motion of Long Jump')

# Add sliders
ax_velocity = plt.axes([0.25, 0.2, 0.65, 0.03])
ax_angle = plt.axes([0.25, 0.15, 0.65, 0.03])

s_velocity = Slider(ax_velocity, 'Velocity (m/s)', 1, 12.34, valinit=10)
s_angle = Slider(ax_angle, 'Takeoff Angle (degrees)', 0, 90, valinit=45)

# Texts for displaying height, distance, and time
text_height = ax.text(0.05, 0.95, '', transform=ax.transAxes)
text_distance = ax.text(0.05, 0.9, '', transform=ax.transAxes)
text_time = ax.text(0.05, 0.85, '', transform=ax.transAxes)

# Define sand color gradient (red)
sand_colors = ['#f4a460', '#ff6347', '#d32f2f', '#b71c1c', '#8b0000', '#8b0000']

# Set background color gradient
ax.set_facecolor(sand_colors[0])
fig.patch.set_facecolor(sand_colors[-1])

# Draw rectangle representing the takeoff board
takeoff_board = plt.Rectangle((0, 0), 3.66, 5, color='black', alpha=0.3)
ax.add_patch(takeoff_board)

# Projectile motion function
def projectile_motion(velocity, angle):
    time_max = 2 * velocity * np.sin(np.radians(angle)) / g
    time_intervals = np.linspace(0, time_max, 100)
    x = velocity * np.cos(np.radians(angle)) * time_intervals
    y = velocity * np.sin(np.radians(angle)) * time_intervals - 0.5 * g * time_intervals**2
    return x, y

# Update function for animation
def update(val):
    velocity = s_velocity.val
    angle = s_angle.val
    x, y = projectile_motion(velocity, angle)
    line.set_data(x, y)
    
    max_height = (velocity**2 * np.sin(np.radians(angle))**2) / (2 * g)
    total_distance = (velocity**2 * np.sin(np.radians(2*angle))) / g
    total_distance_ft = total_distance * 3.28084
    time_in_air = (2 * velocity * np.sin(np.radians(angle))) / g
    
    text_height.set_text(f'Max Height: {max_height:.2f} m')
    text_distance.set_text(f'Total Distance: {total_distance:.2f} m ({total_distance_ft:.2f} ft)')
    text_time.set_text(f'Time in Air: {time_in_air:.2f} s')
    
    # Annotate world record and Olympic record markers
    ax.text(8.95, 3, 'World Record (8.95 m)', ha='center', color='red')
    ax.text(8.90, 3.5, 'Olympic Record (8.90 m)', ha='center', color='blue')
    
    # Add markers for world record and Olympic record
    ax.axvline(x=8.95, linestyle='--', color='red', label='World Record (8.95 m)')
    ax.axvline(x=8.90, linestyle='--', color='blue', label='Olympic Record (8.90 m)')

    return line, text_height, text_distance, text_time

# Function to initialize the plot
def init():
    line.set_data([], [])
    text_height.set_text('')
    text_distance.set_text('')
    text_time.set_text('')
    return line, text_height, text_distance, text_time

# Set up animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True)

# Show plot
plt.show()
