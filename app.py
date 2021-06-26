import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
#from bokeh.plotting import figure, show, ColumnDataSource
import matplotlib.pyplot as plt


st.markdown('''
# Stock Price App
By Mahsa Sharifi
''')
st.write('---')


st.sidebar.subheader('User input')
#Get all the possible tickers from the CSV file tickers.csv
list_tickers = pd.read_csv('tickers.csv') 
Symbol = st.sidebar.selectbox('Choose the ticker here', list_tickers)
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 2, 1))



Data = yf.Ticker(Symbol) 
tickerDataFrame = Data.history(period='1d', start=start_date, end=end_date)


st.header('**Ticker data**')
st.write(tickerDataFrame)



st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.DataFrame(tickerDataFrame.Close)
df['Date'] = df.index
plt.fill_between(df.Date, df.Close, color='blue', alpha=0.5)
plt.plot(df.Date, df.Close, color='red', alpha=0.5)
plt.xticks(rotation=90)
plt.title(Symbol, fontweight='bold')
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Closing Price', fontweight='bold')
st.pyplot()



###Newer versions of bokeh does not work with streamlit :(
#p = figure(plot_width= 400, plot_height=250, x_axis_type="datetime")
#p.title.text = 'Click on legend entries to hide the corresponding lines'

#df = pd.DataFrame(tickerDf)
#df['date'] = df.index
#p.line(df['date'], df['Close'], line_width=2, color= 'skyblue', alpha=0.8, legend=tickerSymbol)

#st.bokeh_chart(p, use_container_width=False)
#show(p)

