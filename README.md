# 🌤️ Weather Forecast Web Application

This project is a simple web application built using Streamlit that provides weather forecasts for any city over a range of 1 to 5 days. The data is fetched from the OpenWeatherMap API and displayed in an easy-to-use interface. Users can choose between viewing temperature trends or sky conditions (like clouds, rain, etc.).

The application is **deployed** and available at: [Weather Forecast App](https://weather-forecast-web-app-cdrjywnmgw4hpfttu7edc4.streamlit.app/), hosted on **Streamlit Cloud**.

## Features
- Get weather forecasts for any location.
- Choose between 1 to 5 days of weather forecasting.
- View temperature trends with interactive line charts.
- View sky conditions (Clear, Clouds, Rain, Snow) with corresponding images.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/weather-forecast-app.git
    ```
3. Navigate into the project directory:

    ```bash
    cd weather-forecast-app
    ```
5. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

7. Get an API key from [OpenWeatherMap](https://openweathermap.org/) by creating an account.

8. Set up your API key as an environment variable:

    ```bash
    export API_KEY=YOUR_API_KEY
    ```

## Usage

1. To run the application locally, use the following command:

    ```bash
    streamlit run main.py
    ```

3. Once the app is running, you can enter a city name and select the number of forecast days (from 1 to 5).

4. You can choose between two data views:
    - **Temperature**: Displays a line chart of temperature trends over the selected days.
    - **Sky Conditions**: Shows images representing sky conditions (e.g., clear, cloudy, rainy) for each time interval.

## Example

### Temperature Forecast for Tokyo (3 days):
![Temperature example](images/temperature_example.png)

### Sky Conditions for London (2 days):
![Sky Conditions example](images/sky_example.png)


