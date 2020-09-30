import csv
import glob
import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay # BDay for business day

#todo temporary definition of constants
def create_stock_df(nr_days_to_trade=100, start_date_str='2017-01-17', nr_days_of_history=10):
    """
    Wrapper for importing the stock data
    """
    return(import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str))


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


# todo do proper check for file not found
# todo temporary limitation of the nr of stocks
def import_stock_data(nr_days_of_history, nr_days_to_trade, start_date_str):
    """
    Imports the relevant data from the text file system as a pandas data frame
    """
    # OBS!!!!!! temporary limitation for the size of the data frame
    size_of_subset = 100
    
    # pick out the desired start and end dates
    dates = calculateDates(nr_days_of_history = nr_days_of_history, nr_days_to_trade = nr_days_to_trade, start_date_str = start_date_str)

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
    #df.reset_index(drop=True)

    return(df)

#window = sys.argv[1]
#start_date = sys.argv[2]
create_stock_df()