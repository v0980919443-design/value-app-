import streamlit as st
import yfinance as yf

st.title("📊 美股價值投資分析")

ticker = st.text_input("請輸入股票代碼（例如 AAPL）")

if ticker:
    stock = yf.Ticker(ticker)
    info = stock.info

    st.write("公司名稱：", info.get("longName"))
    st.write("本益比 PE：", info.get("trailingPE"))
    st.write("ROE：", info.get("returnOnEquity"))
    st.write("負債比：", info.get("debtToEquity"))

    st.write("⚠ 僅供研究用途")
