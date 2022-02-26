import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

def get_info(ticker):
    ticker = yf.Ticker(ticker)
    info_dict = ticker.info
    new_dict = {k:v for k,v in info_dict.items()}
    df = pd.DataFrame.from_dict(new_dict,orient='index')
    return df

def get_historical_data(ticker):
    tick = yf.Ticker(ticker)
    df = tick.history(start = "2021-06-01", end = "2022-02-26")
    table_historical = pd.DataFrame(df)
    return table_historical

def get_recommendations(ticker):
    tick = yf.Ticker(ticker)
    recommendations = tick.recommendations
    df_recco = pd.DataFrame(recommendations)
    return df_recco

def get_financials(ticker):
    tick = yf.Ticker(ticker)
    financials = tick.financials
    df_financials = pd.DataFrame(financials)
    return df_financials

def get_cashflow(ticker):
    tick = yf.Ticker(ticker)
    cashflow = tick.cashflow
    df_cashflow = pd.DataFrame(cashflow)
    return df_cashflow

## Function that plots daily high price over time
def plot_graph_over_time(dataframe):
    fig,ax=plt.subplots()
    ax.plot("High", data = dataframe)
    ax.set_title("Daily High and Volume over Time")
    ax.tick_params(axis = 'x', labelrotation = 45)
    ax.set_ylabel("Daily High (USD)", color = "blue")
    ax2 = ax.twinx()
    ax2.plot("Volume", data = dataframe, color = "red")
    ax2.set_ylabel("Volume", color = "red")
    ax.legend()
    ax2.legend()
    plt.show()

## Function that plots the net income over time
def plot_net_income(dataframe):
    plt.plot("Net Income", data = dataframe)
    plt.title("Net Income over Time")
    plt.xticks(rotation = 45)
    plt.show()


## Get user input for Ticker
stock = input("Please input stock ticker!\n")

## Transform data in DataFrames
table_info = get_info(stock)
df = get_historical_data(stock)
df_recco = get_recommendations(stock)
df_financials = get_financials(stock)
df_cashflow = get_cashflow(stock)
df_cashflow_t = df_cashflow.transpose()


## Print overview (Include please)
print(df[df.index == "2022-02-25"])
print(df_recco.tail(10))

## Show plots
plot_graph_over_time(df)
plot_net_income(df_cashflow_t)
