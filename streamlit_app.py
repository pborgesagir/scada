import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np

def draw_water_funnel_and_pumps(fill_level):
    fig, ax = plt.subplots()

    # Draw water funnel
    funnel_top_width = 5    # Total width of the funnel at the top
    funnel_bottom_width = 2  # Width of the funnel at the bottom
    funnel_height = 10      # Total height of the funnel

    # Points for the funnel
    funnel_verts = [
        (0, 0),  # bottom left
        (funnel_bottom_width, 0),  # bottom right
        ((funnel_top_width - funnel_bottom_width) / 2 + funnel_bottom_width, funnel_height),  # top right
        ((funnel_top_width - funnel_bottom_width) / 2, funnel_height),  # top left
        (0, 0)  # ignored
    ]

    funnel_codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    funnel_path = Path(funnel_verts, funnel_codes)
    funnel_patch = patches.PathPatch(funnel_path, linewidth=1, edgecolor='k', facecolor='none')
    ax.add_patch(funnel_patch)

    # Calculate water level dimensions
    water_level_height = fill_level * funnel_height
    water_bottom_width = funnel_bottom_width + (fill_level * (funnel_top_width - funnel_bottom_width))
    
    # Water level
    water_verts = [
        (0, 0),
        (water_bottom_width, 0),
        ((funnel_top_width - water_bottom_width) / 2 + water_bottom_width, water_level_height),
        ((funnel_top_width - water_bottom_width) / 2, water_level_height),
        (0, 0)
    ]
    water_path = Path(water_verts, funnel_codes)
    water_patch = patches.PathPatch(water_path, linewidth=1, edgecolor='k', facecolor='blue')
    ax.add_patch(water_patch)

    # Draw pumps as circles
    pump_radius = 1  # Radius of the pump circle
    for i in range(3):  # Draw three pumps
        pump_x = funnel_top_width + 2 + (3 * i)
        pump_y = funnel_height / 2
        pump_circle = patches.Circle((pump_x, pump_y), pump_radius, linewidth=1, edgecolor='k', facecolor='grey')
        ax.add_patch(pump_circle)

    # Draw pipelines
    # Main pipeline from funnel to the first pump
    ax.plot([funnel_top_width, funnel_top_width + 2], [funnel_height / 2, funnel_height / 2], 'k-', lw=2)
    
    # Pipelines connecting pumps
    for i in range(2):
        ax.plot([funnel_top_width + 2 + (3 * i) + pump_radius, funnel_top_width + 2 + (3 * (i + 1)) - pump_radius], 
                [funnel_height / 2, funnel_height / 2], 'k-', lw=2)

    # Add warning text if the tank is less than 30% full
    if fill_level < 0.3:
        warning_msg = "Warning: Low water level!"
        ax.text(funnel_top_width / 2, funnel_height / 2, warning_msg, fontsize=12, color='red', ha='center')

    # Customize plot
    ax.set_title('Water Funnel Connected to Hydraulic Pumps')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_xlim(-1, funnel_top_width + 10)
    ax.set_ylim(-1, funnel_height + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    return fig

def main():
    st.title("Water Funnel Connected to Hydraulic Pumps")

    # Display water funnel and pumps diagram
    tank_fill_level = st.slider("Water Funnel Fill Level", 0.0, 1.0, 0.5, step=0.01)
    water_funnel_fig = draw_water_funnel_and_pumps(tank_fill_level)
    st.pyplot(water_funnel_fig)

if __name__ == "__main__":
    main()



