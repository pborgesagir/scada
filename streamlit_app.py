import streamlit as st
import matplotlib.pyplot as plt

def draw_schema(fill_level):
    fig, ax = plt.subplots()

    # Draw water tank
    tank_height = 100
    tank_width = 50
    water_height = fill_level * tank_height

    # Create a rectangle for water tank
    tank = plt.Rectangle((10, 0), tank_width, tank_height, fill=None, edgecolor='b')
    ax.add_patch(tank)

    # Fill the water tank to the specified level
    water = plt.Rectangle((10, 0), tank_width, water_height, color='blue')
    ax.add_patch(water)

    # Draw pumps and pipes
    pumps = [('Pump 1', (80, 40)), ('Pump 2', (80, 80))]
    for pump, pos in pumps:
        ax.text(*pos, pump, ha='center')

    # Draw pipes
    pipe_positions = [
        ((60, 20), (120, 20)),  # Horizontal pipe
        ((60, 60), (120, 60)),  # Horizontal pipe
        ((60, 20), (60, 60)),   # Vertical connecting pipe
        ((120, 20), (120, 60))  # Vertical connecting pipe
    ]
    
    for start, end in pipe_positions:
        line = plt.Line2D((start[0], end[0]), (start[1], end[1]), lw=2, color='black')
        ax.add_line(line)

    # Add flow meters
    flow_meters = [('FM1', (70, 20)), ('FM2', (70, 60))]
    for fm, pos in flow_meters:
        ax.text(*pos, fm, ha='center')

    # Customize plot
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 120)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')  # Turn off the axis

    return fig

def main():
    st.title("Water Tank and Hydraulic Pumps Schema")

    # User input for tank fill level
    tank_fill_level = st.slider("Water Tank Fill Level", 0.0, 1.0, 0.5, step=0.01)

    # Display schema
    schema_fig = draw_schema(tank_fill_level)
    st.pyplot(schema_fig)

if __name__ == "__main__":
    main()

