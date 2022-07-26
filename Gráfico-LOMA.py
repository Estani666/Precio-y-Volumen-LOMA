import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Abajo puede observar el **precio de cierre** y el **volumen** de Loma Negra!
""")

#Aquí agregamos el nombre del Ticker
tickerSymbol = 'LOMA'
#Obtenemos el dato del ticker introducido
tickerData = yf.Ticker(tickerSymbol)
#Obtenemos el historial de precios del ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-12-31')

# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
### Precio de Cierre
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volumen operado
""")
st.line_chart(tickerDf.Volume)