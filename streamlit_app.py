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

def main():
    st.title("HVAC System Diagram")

    # Draw HVAC system diagram
    hvac_fig = draw_hvac_system()

    # Display the diagram in Streamlit
    st.pyplot(hvac_fig)

if __name__ == "__main__":
    main()
