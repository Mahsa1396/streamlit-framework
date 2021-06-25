import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from bokeh.plotting import figure, show, ColumnDataSource
import matplotlib.pyplot as plt

# App title
st.markdown('''
# Stock Price App
By Mahsa Sharifi
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('tickers.csv')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker


# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

#st.set_option('deprecation.showPyplotGlobalUse', False)
#df = pd.DataFrame(tickerDf.Close)
#df['Date'] = df.index
#plt.fill_between(df.Date, df.Close, color='red', alpha=0.3)
#plt.plot(df.Date, df.Close, color='red', alpha=0.8)
#plt.xticks(rotation=90)
#plt.title(tickerSymbol, fontweight='bold')
#plt.xlabel('Date', fontweight='bold')
#plt.ylabel('Closing Price', fontweight='bold')

#st.pyplot()

p = figure(plot_width= 400, plot_height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to hide the corresponding lines'

df = pd.DataFrame(tickerDf)
df['date'] = df.index
p.line(df['date'], df['Close'], line_width=2, color= 'skyblue', alpha=0.8, legend=tickerSymbol)

st.bokeh_chart(p, use_container_width=False)
#show(p)


####
#st.write('---')
#st.write(tickerData.info)
