import streamlit as st
import matplotlib.pyplot as plt

def draw_water_tank_and_hospital(fill_level):
    fig, ax = plt.subplots()

    # Draw water tank
    tank_height = 10  # Total height of the tank
    tank_width = 5    # Total width of the tank
    tank_depth = 3    # Total depth of the tank

    ax.plot([0, tank_width, tank_width, 0, 0], [0, 0, tank_height, tank_height, 0], 'k-')
    water_height = fill_level * tank_height
    ax.fill_between([0, tank_width], [0, 0], [water_height, water_height], color='blue')

    # Draw hospital building
    hospital_width = 8
    hospital_height = 6
    ax.plot([10, 10 + hospital_width, 10 + hospital_width, 10, 10], [0, 0, hospital_height, hospital_height, 0], 'k-')

    # Draw pipelines
    ax.plot([tank_width, 10], [0.5 * tank_height, 0.5 * tank_height], 'k-', lw=2)  # Main pipeline
    ax.plot([10, 10], [hospital_height, hospital_height - 1], 'k-', lw=2)  # Branch pipeline
    ax.plot([10, 10 + hospital_width], [hospital_height - 1, hospital_height - 1], 'k-', lw=2)  # Connection to hospital

    # Customize plot
    ax.set_title('Water Tank Connected to Hospital')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_xlim(-1, 20)
    ax.set_ylim(-1, max(tank_height, hospital_height) + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    return fig

def main():
    st.title("Water Tank Connected to Hospital")

    # Display water tank and hospital diagram
    tank_fill_level = st.slider("Water Tank Fill Level", 0.0, 1.0, 0.5, step=0.1)
    water_tank_fig = draw_water_tank_and_hospital(tank_fill_level)
    st.pyplot(water_tank_fig)

if __name__ == "__main__":
    main()


