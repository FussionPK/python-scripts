import decimal
import streamlit as st
import pandas as pd
import numpy as np

def app():

    #to add a website icon that shows up in the browser tab with with a link to the image we can use the following code

    st.set_page_config(
        page_title="Andy Warhol and his Cylinder Calculator",
        page_icon="https://static.vecteezy.com/system/resources/previews/036/328/613/non_2x/calculator-icon-illustration-for-web-app-infographic-etc-vector.jpg",
        layout="centered",
        initial_sidebar_state="auto",

    )

    with st.sidebar:
        st.header("About")
        st.write("This app provides information about Andy Warhol and allows users to calculate the volume and surface area of a cylinder based on user-inputted radius and height.")
        login_info = """
        ## Login Information
        - Username: admin
        - permission: access to cylinder calculator and Andy Warhol info
        """
        st.markdown(login_info)

    #we are going to display info about andy warhol and an image of him resized to 100x100 pixels
    andy_info = """
    ## Andy Warhol
    Andy Warhol was an American artist, film director, and producer who was a leading figure in the visual art movement known as pop art. His works explore the relationship between artistic expression, culture, and advertisement that flourished by the 1960s. Some of his most famous works include the Campbell's Soup Cans and Marilyn Diptych.

    ![Andy Warhol](https://artlogic-res.cloudinary.com/w_400,h_400,c_fill,f_auto,fl_lossy,q_auto,r_40/ws-benbrownfinearts/usr/images/artists/group_images_override/items/39/3926a038ab63445bb308aec7ea82d2a4/warhol-headshot.jpg)
    """
    st.markdown(andy_info)

    #we will now make the calculator for the cylinder volume and surface area
    st.markdown("## Volume and Surface Area of a Cylinder Calculator")
    cylinder_radius = st.number_input("Enter the radius of the cylinder:", min_value=0.0, format="%.2f")
    cylinder_height = st.number_input("Enter the height of the cylinder:", min_value=0.0, format="%.2f")
    if st.button("Calculate"):
        volume = 3.14 * (cylinder_radius * cylinder_radius) * cylinder_height
        surface = (2 * (3.14 * (cylinder_radius * cylinder_radius))) + (2 * (3.14 * cylinder_radius * cylinder_height))
        st.markdown(f"The volume of the cylinder is to 2 decimal places: {round(volume, 2)}")
        st.markdown(f"The surface area of the cylinder is to 2 decimal places: {round(surface, 2)}")

        st.markdown(f"The surface area of the cylinder is to 2 decimal places: {round(surface, 2)}")
    elif st.button("Clear"):
        st.experimental_rerun()

    #i will now add a chart display
    st.markdown("## Sample Data Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=["London", "New York", "Tokyo","Dubai"]
    )

    chart_data_2 = pd.DataFrame(
        np.random.randn(10,3),
        columns=["a","b","c"]
    )

    chart_data_3 = pd.DataFrame(
        np.random.randn(10,3),
        columns=["x","y","z"]
    )

    #to now display one chart with three buttons under it that load the different charts when clicked
    chart_type = st.radio(
        "Select Chart Type",
        ("Line Chart", "Bar Chart", "Area Chart"),
        horizontal=True
    )

    #now i want to display the chart

    if chart_type == "Line Chart":
        st.line_chart(chart_data)
    elif chart_type == "Bar Chart":
        st.bar_chart(chart_data_2)
    elif chart_type == "Area Chart":
        st.area_chart(chart_data_3) 

    #to make the app more visually appealing we can add some custom CSS styles
    
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
#in order to display the app when run directly
if __name__ == "__main__":
    app()

#this works because __name__ is set to __main__ when the script is run directly what these two mean 
#is that if this script is run directly, the app() function will be called and the Streamlit app will be displayed.
#next we will build a login page for the app

