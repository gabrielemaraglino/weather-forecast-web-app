import streamlit as st
import plotly.express as px
from backend import get_data


def plot_temperature(dates, temperatures):
    """Generate a temperature line plot."""
    figure = px.line(x=dates, y=temperatures,
                     labels={"x": "Date", "y": "Temperature (°C)"},
                     title="Temperature Forecast")
    st.plotly_chart(figure)


def display_sky_conditions_with_info(filtered_data, images):
    """Display weather condition images with date and time below."""
    cols = st.columns(4)  # Display 3 images per row for better size and visibility
    for idx, entry in enumerate(filtered_data):
        condition = entry["weather"][0]["main"]
        date_time = entry["dt_txt"]
        image_path = images.get(condition, "images/default.png")

        # Use columns dynamically, moving to a new row after every 3 items
        with cols[idx % 4]:
            st.image(image_path, width=150)  # Increased image size
            st.write(f"**{condition}**")  # Display the sky condition (e.g., "Clear")
            st.markdown(f"<p style='font-size:14px;'>{date_time}</p>",
                        unsafe_allow_html=True)  # Slightly larger date/time


# Add title and user inputs
st.title("🌤️ Weather Forecast for the Next Days")
place = st.text_input("Enter a location: ")
days = st.slider("Select number of forecast days", min_value=1, max_value=5,
                 help="Select the number of days for the weather forecast")
option = st.selectbox("Choose data type", ("Temperature", "Sky Conditions"))

if place:
    st.subheader(f"Weather forecast for {days} day(s) in {place}")

    # Show a loading spinner while fetching data
    with st.spinner('Fetching data...'):
        filtered_data = get_data(place, days)

    if isinstance(filtered_data, str):  # In case of error message
        st.error(filtered_data)
    else:
        if option == "Temperature":
            # Extract and plot temperature data
            temperatures = [entry["main"]["temp"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            plot_temperature(dates, temperatures)

        elif option == "Sky Conditions":
            # Extract and display sky condition images with date and time
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            display_sky_conditions_with_info(filtered_data, images)