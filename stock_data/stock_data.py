import csv
import glob
import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay # BDay for business day

def create_stock_df(nr_days_to_trade=1, start_date_str='2017-01-17', nr_days_of_history=1):
    """
    Wrapper for importing the stock data
    """

    print(import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str).to_csv())
   # return(import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str))

def calculateDates(nr_days_of_history, nr_days_to_trade, start_date_str):
    """
    Calculates correct start and end dates for the data frame.
    - The start date is moved backward in order to include the history_window for the first day of trading.
    """

    # create a start date
    start_date = pd.Timestamp(start_date_str)

    # add end date
    end_date = start_date + BDay(nr_days_to_trade)

    # include a history window for first day
    start_date = start_date - BDay(nr_days_of_history)

    return {'start_date':start_date,'end_date':end_date}


def read_in_as_list_of_dfs(all_files,start_date,end_date):
    """
    Create list of cleaned data frames of the stock data in the specified files
    """
    # create an empty list to add each (relevant) stock's data frame
    li=[]

    # go through all the files in the folder
    for filename in all_files:
        # read in the file
        df = pd.read_csv(filename, parse_dates=[0])
        
        # basic trimming: drop all extra columns,rename the stock value column after the stock
        df = df.drop(labels=list(['volume','close','high','low','adjclose']), axis='columns') 
        stock_name = filename.split(sep='/')[4].split(sep='.')[0].lower()
        df = df.rename(columns={'open': stock_name})
        
        # fit to time window: selct only rows with relevant dates and ignore stocks without relevant values
        df = df.loc[(df['date'] > start_date) & (df['date'] < end_date)]
        if df.empty:
            continue
        
        # prepare to join on dates 
        df=df.set_index('date')

        # remove duplicates
        df = df.loc[np.logical_not(df.index.duplicated())]

        # add to list of dfs
        li.append(df)

    return(li)


def clean_combined_df(df):
    """
    Reduce the size and time unnecessary info (date)
    """
    # remove dates (anonymises the time window somewhat)
    df = df.reset_index(drop=True)

    # set non-existing recordings to zero (stock had zero value at the time)
    df = df.fillna(0)

    # select the smallest suitable type of float for the data
    df = df.astype(np.float16)

    return(df)
 

def import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str):
    """
    Imports the relevant data from the text file system as a pandas data frame
    """
    
    # pick out the desired start and end dates
    dates = calculateDates(nr_days_of_history = nr_days_of_history, nr_days_to_trade = nr_days_to_trade, start_date_str = start_date_str)

    # list the files to be read
    #path = "./data/full_history/*.csv"
    path = "../stock_data/data/full_history/*.csv"
    all_files = np.array(glob.glob(path))

    # read in the data frames from the files
    li = read_in_as_list_of_dfs(all_files, dates['start_date'], dates['end_date'])

    # combine into a single data frame
    df = pd.concat(li, join='outer', axis=1)

    # clean the combined data frame
    df = clean_combined_df(df)

    return(df)

#window = sys.argv[1]
#start_date = sys.argv[2]
create_stock_df()