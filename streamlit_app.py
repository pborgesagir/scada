import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

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
    ax.plot([10, 10 + hospital_width, 10 + hospital_width, 10, 10], [-1, -1, hospital_height, hospital_height, 0], 'k-')

    # Draw pipelines
    ax.plot([5, 10], [0.05 * tank_height, 0.05 * tank_height], 'k-', lw=4)  # Main pipeline
    ax.plot([10, 10], [hospital_height, hospital_height - 7], 'k-', lw=2)  # Branch pipeline
    ax.plot([10, 10 + hospital_width], [hospital_height - 1, hospital_height - 1], 'k-', lw=2)  # Connection to hospital
    ax.plot([0, 1.5], [0, -2.5], 'k-', lw=2)
    ax.plot([5, 3.5], [0, -2.5], 'k-', lw=2)
    ax.plot([1.5, 1.5], [-2.5, -9.5], 'k-', lw=2)
    ax.plot([3.5, 3.5], [-2.5, -9.5], 'k-', lw=2)
    ax.plot([1.5, 3.5], [-9.5, -9.5], 'k-', lw=2)
    ax.plot([3.5, 20], [-9.5, -9.5], color='grey', lw=1.8)
    ax.plot([20, 20], [-9.5, -15], color='grey', lw=1.8)
    ax.plot([20, 22.5], [-15, -15], color='grey', lw=1.8)
    ax.plot([20, 22.5], [-15, -15], color='grey', lw=1.8)
    
    #bomba
    ax.add_patch(Circle((22.5, -15), 2, color='darkgray', lw=1.8))
    ax.add_patch(Circle((22.5, -15), 2, fill=False, color='black', lw=1.8))
    ax.add_patch(Circle((22.5, -15), 0.5, fill=False, color='black', lw=0.8))
    ax.plot([22, 21], [-15, -18], color='black', lw=1.8)
    ax.plot([23, 24], [-15, -18], color='black', lw=1.8)
    ax.plot([21, 24], [-18, -18], color='black', lw=1.8)
    # Write "B1" below the pump
    ax.text(22.5, -20, "B1", color='orange', ha='center')

    #pipes
    ax.plot([24.5, 30], [-14, -14], color='grey', lw=1.8)
    ax.plot([30, 35], [-14, -5], color='grey', lw=1.8)
    
    
   
    
    

    # Customize plot
    ax.set_title('Volume de Água na Caixa dÁgua')
    # ax.set_xlabel('Width')  # Removed
    # ax.set_ylabel('Height')  # Removed
    ax.set_xlim(-5, 65)
    ax.set_ylim(-35, max(tank_height, hospital_height) + 10)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    
    # Remove axis ticks and labels
    #ax.set_xticks([])
    #ax.set_yticks([])
    #ax.xaxis.set_ticklabels([])
    #ax.yaxis.set_ticklabels([])

    return fig

def main():
    st.title("Volume de Água na Caixa d'Água")

    # Display water tank and hospital diagram
    tank_fill_level = st.slider("Water Tank Fill Level", 0.0, 1.0, 0.5, step=0.1)
    water_tank_fig = draw_water_tank_and_hospital(tank_fill_level)
    st.pyplot(water_tank_fig)

if __name__ == "__main__":
    main()

