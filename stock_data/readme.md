How to import the stock data
===

- The data has to be in this folder, so that the path "./data/full_history/*.csv" finds all csv files.

- To start importing data, call the stock_data.py file. 

The function 'create_stock_df(nr_days_to_trade, start_date_str, nr_days_of_history)' is a wrapper for the file with the default values 500, 2017-01-17, 10. Currently, the file wrapper is also called when simply running the file (see the end of the file).
