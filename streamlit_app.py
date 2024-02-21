import streamlit as st
import matplotlib.pyplot as plt

def draw_hvac_system():
    fig, ax = plt.subplots()

    # Draw HVAC components
    ax.plot([0, 3], [1, 1], 'k-', lw=3)  # Main duct
    ax.plot([3, 3], [1, 2], 'k-', lw=3)  # Branch duct
    ax.plot([3, 5], [1, 1], 'k-', lw=3)  # Room duct
    ax.add_patch(plt.Circle((3, 1), 0.2, color='gray'))  # Fan
    ax.plot([5, 6], [1, 1], 'k-', lw=3)  # Vent
    ax.plot([5, 6], [1, 2], 'k-', lw=3)  # Return vent

    # Customize plot
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    ax.set_title('HVAC System')

    return fig

def display_water_tank(fill_level):
    tank_height = 10  # Total height of the tank
    tank_width = 5    # Total width of the tank
    tank_depth = 3    # Total depth of the tank

    fig, ax = plt.subplots()

    # Draw tank outline
    ax.plot([0, tank_width, tank_width, 0, 0], [0, 0, tank_height, tank_height, 0], 'k-')

    # Draw water level
    water_height = fill_level * tank_height
    ax.fill_between([0, tank_width], [0, 0], [water_height, water_height], color='blue')

    # Customize plot
    ax.set_title('Water Tank')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_xlim(-1, tank_width + 1)
    ax.set_ylim(-1, tank_height + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    return fig

def main():
    st.title("HVAC System and Water Tank Visualization")

    # Draw HVAC system diagram
    hvac_fig = draw_hvac_system()

    # Display HVAC system diagram in Streamlit
    st.pyplot(hvac_fig)

    # Display water tank visualization in Streamlit
    tank_fill_level = st.slider("Water Tank Fill Level", 0.0, 1.0, 0.5, step=0.1)
    water_tank_fig = display_water_tank(tank_fill_level)
    st.pyplot(water_tank_fig)

if __name__ == "__main__":
    main()

