import sys, json
import pandas as pd

def parse_stocks_as_df(dict_stocks):
    li=[]
    for stock in dict_stocks:
        df = pd.DataFrame(stock)
        
        # just in case  
        if df.empty:
            continue
        
        # basic trimming: drop all extra columns,rename the stock value column after the stock
        df = df.drop(labels=list(['name','id']), axis='columns')
        df = df.rename(columns={'value': stock['id']})

        li.append(df)

    # combine into a single data frame
    df_stocks = pd.concat(li, join='outer', axis=1)

    df_stocks.index.name = 'day'

    return(df_stocks)
    
# replace this line with input from js
js_input_dict = json.loads(sys.argv[1])

capital_available = js_input_dict['capital']
df_stocks = parse_stocks_as_df(js_input_dict['stocks'])
df_port = pd.DataFrame(js_input_dict['portfolio']).set_index('stocks')

print('Current capital available is ' + str(capital_available) + '.\n')
print('Current portfolio is\n' + str(df_port) + '\n')
print('The available stocks, presented with their stockvalue for the last n days, are:\n' + str(df_stocks) + '\n')



# export type StockAction = {
#     stockId: number,
#     quantity: number,
# };