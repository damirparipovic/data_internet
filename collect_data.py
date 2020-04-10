#!/usr/bin/env python

# Imoprts
import sys
import speedtest
import datetime
import pandas as pd
import os
from pathlib import Path


# Constants
cols = ['download', 'upload', 'ping', 'server', 'timestamp', 'bytes_sent',
       'bytes_received', 'share', 'client']        # Columns are in order that is returned by speedtest lib.

data_folder = Path("./data")        # Path object, allows for better filename/path manipulation and checking.

# Functions

def file_check(file):
    '''Checks whether a file exists at given filepath and if it doesn't
    call the create_file() function.'''

    if file.exists():
        print(f"File {file.name} exists.")
        
    else:
        print(f"File {file.name} does not exist.")
        create_file(file)
        file_check(file)


def create_file(filepath):
    '''Creates a file at filepath.'''

    with open(filepath, "w") as f:
        print(f"File created at {filepath}.")
        f.close()

def collect_data():
    ''' Collects the internet speed data in a dictionary. The dictionary
        is formatted for pandas. The final dictionary is returned.''' 

    curr_conection = speedtest.Speedtest()
    curr_conection.download()
    curr_conection.upload()

    results = curr_conection.results.dict()

    formated_results = {k : [v] for k, v in results.items()}

    return formated_results

def convert_to_mb(speed):
    '''Converts given internet speed from bits/s to Megabytes/s'''
    return (speed / 8) / 10**6

def convert_to_kb(speed):
    '''Converts given internet speed from bits/s to Kilobytes/s'''
    return (speed / 8) / 10**3


def main():

    new_df = False      # flag for whether the dataframe is new or not

    year = datetime.datetime.today().year       # current year
    month = datetime.datetime.today().month     # current month

    file_name = f"{year}_{month}.csv"

    file_to_open = data_folder / file_name

    file_check(file_to_open)

    try:
        existing_df = pd.read_csv(file_to_open)
    except:
        existing_df = pd.DataFrame()
        new_df = True

    inter_speed = collect_data()    # dictionary containing the relevant internet speed data
    
    print(existing_df)

    inter_speed["timestamp"] = datetime.datetime.now()
    df = pd.DataFrame(inter_speed)
    print(df)

    if new_df:
        existing_df = df
    else:
        existing_df = pd.concat([existing_df, df], ignore_index=True)

    print(existing_df)

    existing_df.to_csv(file_to_open, index=False)

    print("Data collection complete.")

    return 1

# want ignore_index=True (doesn't matter the current index). Better if index represents order added
if __name__ == "__main__":

    main()