import csv
import glob
import numpy as np
import pandas as pd
import sys, json

def create_stock_df(window, start_date):
    # TODO: temp solution
    window = 1000
    start_date = pd.Timestamp('2018-01-17')

    # # TODO:
    # add end date
    # end_date =

    # list the files to be read
    path = "./data/full_history/*.csv"
    all_files = np.array(glob.glob(path))

    # create an empty list to add each stocks data frame
    li=[]

    for filename in all_files[1:100]:
        # read om the file
        df = pd.read_csv(filename, parse_dates=[0])

        # drop all extra columns
        df = df.drop(labels=list(['volume','close','high','low','adjclose']), axis='columns')

        # rename the stock value column after the stock
        stock_name = filename.split(sep='/')[3].split(sep='.')[0].lower()
        df = df.rename(columns={'open': stock_name})

        # select only relevant date
        df = df.loc[df['date'] > start_date]

        # if the stock has no data after the start date, do not add it
        if df.empty:
            continue

        df = df[:window]

        # set index as date in order to join
        df=df.set_index('date')

        # add to the list
        li.append(df)

    # combine all the data frames into one large
    df = pd.concat(li, join='outer', axis=1)

    return df

#window = sys.argv[1]
#start_date = sys.argv[2]
create_stock_df('window', 'start_date')
