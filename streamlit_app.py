import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_water_tank_and_pumps(fill_level):
    fig, ax = plt.subplots()

    # Draw water tank as a funnel
    tank_height = 10  # Total height of the tank
    tank_top_width = 8    # Total top width of the tank (wider part)
    tank_bottom_width = 3  # Bottom width of the tank (narrow part)
    
    # Coordinates for the funnel shape (top-left, top-right, bottom-right, bottom-left)
    tank_coords = [
        (0, tank_height),  # top-left
        (tank_top_width, tank_height),  # top-right
        (tank_top_width / 2 + tank_bottom_width / 2, 0),  # bottom-right
        (tank_top_width / 2 - tank_bottom_width / 2, 0)  # bottom-left
    ]
    
    tank_polygon = patches.Polygon(tank_coords, closed=True, linewidth=1, edgecolor='k', facecolor='none')
    ax.add_patch(tank_polygon)

    # Calculate water level coordinates within the funnel
    # Assuming linear decrease in width with height
    water_top_width = tank_bottom_width + (tank_top_width - tank_bottom_width) * (fill_level)
    water_coords = [
        (tank_top_width / 2 - water_top_width / 2, fill_level * tank_height),
        (tank_top_width / 2 + water_top_width / 2, fill_level * tank_height),
        (tank_top_width / 2 + tank_bottom_width / 2, 0),
        (tank_top_width / 2 - tank_bottom_width / 2, 0)
    ]
    
    water_polygon = patches.Polygon(water_coords, closed=True, linewidth=1, edgecolor='k', facecolor='blue')
    ax.add_patch(water_polygon)

    # Set the limits of the plot
    ax.set_xlim(-1, max(tank_top_width, tank_bottom_width) + 1)
    ax.set_ylim(0, tank_height + 1)
    
    # Show the plot
    plt.show()

# Example usage:
draw_water_tank_and_pumps(0.5)  # Fill level as a fraction of tank height (e.g., 0.5 for 50% full)


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




