import pandas_datareader.data as web

df = web.DataReader("8358.two", 'yahoo', "2020-01-30","2021-12-31")
# df[['Adj Close', 'Volume']].plot(subplots=True);
print(df)