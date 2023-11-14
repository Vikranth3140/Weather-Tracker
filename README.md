# Weather Tracker ☁️

## Overview
Weather Tracker is a simple Python application built with Streamlit that allows users to check the current weather of a city. It utilizes the OpenWeatherMap API to retrieve weather information.

## Prerequisites
Make sure you have the following installed on your system:
- Python
- Streamlit
- Requests library

You can install the required dependencies using the following:
```bash
pip install streamlit requests
```

## Usage
1. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace the `api_key` variable in the script with your key.
2. Run the script: 
    ```bash
    streamlit run <filename>.py
    ```
3. Enter the desired city name in the prompted text input.
4. The application will display the coordinates of the city if it exists; otherwise, it will prompt you to enter a correct city name.

## Example
```python
python weather_tracker.py
```

## Note
Ensure you keep your API key confidential and do not share it publicly.

## Author
[Vikranth Udandarao](https://github.com/Vikranth3140)