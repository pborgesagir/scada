import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_water_tank_and_pumps(fill_level):
    fig, ax = plt.subplots()

    # Draw water tank
    tank_height = 10  # Total height of the tank
    tank_width = 5    # Total width of the tank

    # Create rectangle for the water tank
    tank_rect = patches.Rectangle((0, 0), tank_width, tank_height, linewidth=1, edgecolor='k', facecolor='none')
    ax.add_patch(tank_rect)

    # Create blue rectangle for the water level
    water_rect = patches.Rectangle((0, 0), tank_width, fill_level * tank_height, linewidth=1, edgecolor='k', facecolor='blue')
    ax.add_patch(water_rect)

    # Draw pumps as circles
    pump_radius = 1  # Radius of the pump circle
    for i in range(3):  # Draw three pumps
        pump_x = tank_width + 2 + (3 * i)
        pump_y = tank_height / 2
        pump_circle = patches.Circle((pump_x, pump_y), pump_radius, linewidth=1, edgecolor='k', facecolor='grey')
        ax.add_patch(pump_circle)

    # Draw pipelines
    # Main pipeline from tank to the first pump
    ax.plot([tank_width, tank_width + 2], [tank_height / 2, tank_height / 2], 'k-', lw=2)
    
    # Pipelines connecting pumps
    for i in range(2):
        ax.plot([tank_width + 2 + (3 * i) + pump_radius, tank_width + 2 + (3 * (i + 1)) - pump_radius], 
                [tank_height / 2, tank_height / 2], 'k-', lw=2)

    # Add warning text if the tank is less than 30% full
    if fill_level < 0.3:
        warning_msg = "Warning: Low water level!"
        ax.text(tank_width / 2, tank_height / 2, warning_msg, fontsize=12, color='red', ha='center')

    # Customize plot
    ax.set_title('Water Tank Connected to Hydraulic Pumps')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_xlim(-1, tank_width + 10)
    ax.set_ylim(-1, tank_height + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    return fig

def main():
    st.title("Water Tank Connected to Hydraulic Pumps")

    # Display water tank and pumps diagram
    tank_fill_level = st.slider("Water Tank Fill Level", 0.0, 1.0, 0.5, step=0.01)
    water_tank_fig = draw_water_tank_and_pumps(tank_fill_level)
    st.pyplot(water_tank_fig)

if __name__ == "__main__":
    main()




