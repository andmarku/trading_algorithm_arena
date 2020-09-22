import csv
import glob
import numpy as np
import pandas as pd
<<<<<<< HEAD
<<<<<<< HEAD
from pandas.tseries.offsets import BDay # BDay for business day
=======
>>>>>>> updated with respect to time window and improved comments
=======
from pandas.tseries.offsets import BDay # BDay for business day
>>>>>>> updated dates etc

def calculateDates(small_window, window, start_date):
    # create a start date
    start_date = pd.Timestamp(start_date)

    # add end date
    end_date = start_date + BDay(window)

    # include a history window for first day
    start_date = start_date - BDay(small_window)

    return {'start_date':start_date,'end_date':end_date}

def import_stock_data(window, start_date):
    # temporary definition of constants
    size_of_subset = 100, small_window = 10, window = 500, date_str = '2018-01-17'

    # pick out the desired start and end dates
    dates = calculateDates(small_window = small_window, window = window, start_date = date_str)

    # list the files to be read
    path = "./data/full_history/*.csv"
    all_files = np.array(glob.glob(path))

    # create an empty list to add each (relevant) stock's data frame
    li=[]

    # go through all the files in the folder
    for filename in all_files[:size_of_subset]:
        # read in the file
        df = pd.read_csv(filename, parse_dates=[0])
        
        # basic trimming: drop all extra columns,rename the stock value column after the stock
        df = df.drop(labels=list(['volume','close','high','low','adjclose']), axis='columns') 
        stock_name = filename.split(sep='/')[3].split(sep='.')[0].lower()
        df = df.rename(columns={'open': stock_name})
        
        # fit to time window: selct only rows with relevant dates and ignore stocks without relevant values
        df = df.loc[(df['date'] > dates['start_date']) & (df['date'] < dates['end_date'])]
        if df.empty:
            continue
        
        # prepare for concatenation: prep to join on dates and add to list of dfs
        df=df.set_index('date')
        li.append(df)

    # combine into a single data frame
    df = pd.concat(li, join='outer', axis=1)

    # remove dates (anonymises the time window somewhat)
    df.reset_index(drop=True)

<<<<<<< HEAD
<<<<<<< HEAD
    return(df)
=======
    return df
>>>>>>> updated with respect to time window and improved comments
=======
    return(df)
>>>>>>> updated dates etc
