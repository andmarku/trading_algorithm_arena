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


"""
Parsing the input
"""
js_input_dict = json.loads(sys.argv[1])
capital_available = js_input_dict['capital']
df_stocks = parse_stocks_as_df(js_input_dict['stocks'])
df_port = pd.DataFrame(js_input_dict['portfolio']).rename(columns={'stocks': 'id'})

# code for testing input
# print('Current capital available is ' + str(capital_available) + '.\n')
# print('Current portfolio is\n' + str(df_port) + '\n')
# print('The available stocks, presented with their stockvalue for the last n days, are:\n' + str(df_stocks) + '\n')

"""
Start here!
"""
# fill in clever algorithms for buying and selling
def which_stocks_to_sell(df_port):
    """
    dummy algorithm which sells all stocks
    """
    actions = []
    for i in range(0, df_port.index.size):
        stock_to_sell = df_port.loc[i]

        stock_action = {
            'stockId': stock_to_sell.id,
            'quantity': stock_to_sell.shares,
            'selling': True
        }

        actions.append(stock_action)
        
    return(actions)

def which_stocks_to_buy(capital_to_invest, stocks_df):
    """
    dummy algorithm which buys as much as possible of the cheapest stock
    """
    actions = []

    df = df_stocks.tail(1).iloc[0]
    df = df.loc[~(df==0)]
    stock_with_lowest_value = df.loc[(df==df.min())]
    
    value = int(stock_with_lowest_value)
    quantity = int(capital_to_invest / value)

    stock_action = {
            'stockId': stock_with_lowest_value.index[0],
            'quantity': quantity,
            'selling': False
    }

    actions.append(stock_action)

    return(actions)

# return the selected actions
sell_actions = which_stocks_to_sell(df_port)
buy_actions = which_stocks_to_buy(capital_available, df_stocks)
all_actions = sell_actions + buy_actions
for dict in all_actions:
    print(dict)
