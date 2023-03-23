import pandas as pd
from datetime import datetime, timedelta

# Pulls in and reads the CSV file exported from Outlook 
#  How? - Python uses a package called pandas
df = pd.read_csv('annies_calendar.csv')

# Convert the 'Start Time' and 'End Time' columns to datetime format
# How? - Use the datetime module to work with dates and times 
# A datetime format is a way to represent dates, times, and timestamps as a string - "YYYY-MM-DD HH:MM:SS"
# Y: year (four digits)
# m: month (two digits)
# d: day (two digits)

df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])

# Calculate the duration of each calendar event (in days/hours)
df['Duration (hour)'] = (df['End Time'] - df['Start Time'])

# Calculate the duration of each calendar event in minutes
df['Duration (min)'] = (df['End Time'] - df['Start Time']) / timedelta(minutes=1)

# Group the calendar events by 'Subject' and sum the duration for each group
task_times_hours = df.groupby('Subject')['Duration (hour)'].sum()

# Group the calendar events by 'Subject' and sum the duration for each group
task_times_minutes = df.groupby('Subject')['Duration (min)'].sum()

# Print out the total time spent on each task
print(task_times_hours)

# Print out the total time spent on each task in minutes
print(task_times_minutes)

# Now we're going to try slice these strings to group them together
 