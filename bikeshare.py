import pandas as pd

CITY_DATA = {
    'chicago': 'data/chicago.csv',
    'new york city': 'data/new_york_city.csv',
    'washington': 'data/washington.csv'
}

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    if day != 'all':
        df = df[df['day_of_week'] == day.lower()]

    return df

def compute_time_stats(df):
    common_month = int(df['month'].mode()[0])
    common_day = df['day_of_week'].mode()[0]
    common_hour = int(df['hour'].mode()[0])
    return common_month, common_day, common_hour

def compute_station_stats(df):
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['trip'].mode()[0]
    return common_start_station, common_end_station, common_trip

def compute_trip_duration_stats(df):
    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()
    return total_duration, mean_duration

def compute_user_stats(df):
    user_types = df['User Type'].value_counts().to_dict()
    gender_counts = {}
    birth_year_stats = {}

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts().to_dict()

    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        birth_year_stats = {
            'earliest': earliest_year,
            'most_recent': most_recent_year,
            'most_common': most_common_year
        }

    return user_types, gender_counts, birth_year_stats
