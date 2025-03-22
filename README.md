# Bike Share Data Analysis Project

This project analyzes bike share data for three major U.S. cities: **Chicago**, **New York City**, and **Washington, DC**. The goal is to explore usage patterns, compute descriptive statistics, and provide an interactive terminal experience for users to filter and view data.

## Project Overview
- **Data**: Includes trip details such as start/end times, stations, trip duration, user type, and (for Chicago and NYC) gender and birth year.
- **Tasks**:
  - Compute statistics on popular times of travel, stations, trip duration, and user info.
  - Create an interactive terminal experience to filter and display data.
- **Script**: The `bikeshare.py` script is used to analyze the data and interact with users.

## Dataset
The dataset contains randomly selected data for the first six months of 2017 for all three cities. The data files are:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

Due to the large size of the dataset, the files are provided in a zipped folder. You can download the dataset from the following link:

[Download Zip File](https://drive.google.com/file/d/1rlLjAYB-SRhgVn5puhnSK8YBxjXq6HGh/view?usp=sharing)

## Features
1. **Interactive Terminal Experience**:
   - Users can filter data by city, month, and day.
   - Users can view raw data in chunks of 5 rows at a time.
2. **Statistics Computed**:
   - Popular times of travel (most common month, day, hour).
   - Popular stations and trips (most common start station, end station, and trip).
   - Trip duration (total and average travel time).
   - User info (counts of user types, gender, and birth year for Chicago and NYC).

## How to Run the Project
1. **Download the Zip File**:
   - Use the provided [Google Drive link](https://drive.google.com/file/d/1rlLjAYB-SRhgVn5puhnSK8YBxjXq6HGh/view?usp=sharing) to download the zipped file.
   - Extract the files into the project directory.

2. **Setup & Installation**:
   - Install Python 3 if not already installed.
   - Create and activate a virtual environment** (recommended): env\Scripts\activate (on Windows) or python -m venv env env\Scripts\activate (on Windows)
   
   - Install dependencies :  pip install -r requirements.txt  
   - Place CSV files (chicago.csv, new_york_city.csv, washington.csv) in the `data` folder if not already present.
3. **Usage Instructions**
- Run the application: python main_app.py  
- Open `http://127.0.0.1:5000/` in your web browser:
- Home Page: Overview and quick links.
- Filter Page: Select city, month, and/or day.
- Results Page : Displays computed stats (popular times, stations, trip durations, user info).
- Raw Data Page : Shows 5 rows of raw data at a time, with “Next” and “Back” options.

## Dependencies
- Python 3
- pandas
- NumPy
