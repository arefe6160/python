import streamlit as st
from constants import CURRENCIES
from main import get_exchange_rate, convert_currency
st.title(':dollar: currency converter')
st.markdown("""this tool allows you to instantly convert between different currencies.
            
Enter the amount and choose the currencies to see results.""")

base_currency = st.selectbox('Base currency', CURRENCIES)
target_currency = st.selectbox('Target currency', CURRENCIES)
amount = st.number_input('Amount', min_value=0.0, value=100.0)
if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate is None:
        st.error('Failed to fetch exchange rate. Please try again later.')

    converted_amount = convert_currency(amount, exchange_rate)
    st.success(f"{amount} {base_currency} is {converted_amount} {target_currency}")
    st.success(f"exchange rate:{exchange_rate:.1f}")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="base_currency", value=f"{amount} {base_currency}")
    col3.metric(label="target_currency", value=f"{converted_amount} {target_currency}")
    col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")