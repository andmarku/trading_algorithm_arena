import csv
import glob
import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay # BDay for business day

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def create_stock_df(nr_days_to_trade=500, start_date_str='2017-01-17', nr_days_of_history=10):
    """
    Wrapper for importing the stock data
    """

=======
=======
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a
#todo temporary definition of constants
def create_stock_df(nr_days_to_trade=100, start_date_str='2017-01-17', nr_days_of_history=10):
    """
    Wrapper for importing the stock data
    """
<<<<<<< HEAD
>>>>>>> many small improvements and more comments
=======
def create_stock_df(nr_days_to_trade=500, start_date_str='2017-01-17', nr_days_of_history=10):
    """
    Wrapper for importing the stock data
    """

>>>>>>> improved data cleaning: fixed bug in data (duplicates) and reduced the size of the total date frame
=======
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a
    return(import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str))


def calculateDates(nr_days_of_history, nr_days_to_trade, start_date_str):
    """
    Calculates correct start and end dates for the data frame.
    - The start date is moved backward in order to include the history_window for the first day of trading.
    """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> many small improvements and more comments
=======

>>>>>>> improved data cleaning: fixed bug in data (duplicates) and reduced the size of the total date frame
=======
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a
    # create a start date
    start_date = pd.Timestamp(start_date_str)

    # add end date
    end_date = start_date + BDay(nr_days_to_trade)

    # include a history window for first day
    start_date = start_date - BDay(nr_days_of_history)

    return {'start_date':start_date,'end_date':end_date}

<<<<<<< HEAD
<<<<<<< HEAD
=======

def read_in_as_list_of_dfs(all_files,start_date,end_date):
    """
    Create list of cleaned data frames of the stock data in the specified files
    """
<<<<<<< HEAD
=======

# todo do proper check for file not found
# todo temporary limitation of the nr of stocks
def import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str):
    """
    Imports the relevant data from the text file system as a pandas data frame
    """
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a
    # OBS!!!!!! temporary limitation for the size of the data frame
    size_of_subset = 100
    
    # pick out the desired start and end dates
    dates = calculateDates(nr_days_of_history = nr_days_of_history, nr_days_to_trade = nr_days_to_trade, start_date_str = start_date_str)

    # list the files to be read
    path = "./data/full_history/*.csv"
    all_files = np.array(glob.glob(path))
>>>>>>> many small improvements and more comments

def read_in_as_list_of_dfs(all_files,start_date,end_date):
    """
    Create list of cleaned data frames of the stock data in the specified files
    """
=======
>>>>>>> improved data cleaning: fixed bug in data (duplicates) and reduced the size of the total date frame
    # create an empty list to add each (relevant) stock's data frame
    li=[]

    # go through all the files in the folder
    for filename in all_files:
        # read in the file
        df = pd.read_csv(filename, parse_dates=[0])
        
        # basic trimming: drop all extra columns,rename the stock value column after the stock
        df = df.drop(labels=list(['volume','close','high','low','adjclose']), axis='columns') 
        stock_name = filename.split(sep='/')[3].split(sep='.')[0].lower()
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
    path = "./data/full_history/*.csv"
    all_files = np.array(glob.glob(path))

    # read in the data frames from the files
    li = read_in_as_list_of_dfs(all_files, dates['start_date'], dates['end_date'])

    # combine into a single data frame
    df = pd.concat(li, join='outer', axis=1)

<<<<<<< HEAD
<<<<<<< HEAD
    # clean the combined data frame
    df = clean_combined_df(df)
=======
    # remove dates (anonymises the time window somewhat)
    #df.reset_index(drop=True)
<<<<<<< HEAD
>>>>>>> many small improvements and more comments
=======
    # clean the combined data frame
    df = clean_combined_df(df)
>>>>>>> improved data cleaning: fixed bug in data (duplicates) and reduced the size of the total date frame
=======
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a

    return(df)

#window = sys.argv[1]
#start_date = sys.argv[2]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
create_stock_df()
=======
create_stock_df()
>>>>>>> many small improvements and more comments
=======
create_stock_df()
>>>>>>> improved data cleaning: fixed bug in data (duplicates) and reduced the size of the total date frame
=======
create_stock_df()
>>>>>>> dcd0796669f0f59854099289b306ae2caa5b3f8a
