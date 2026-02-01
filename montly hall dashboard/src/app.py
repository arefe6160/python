import streamlit as st
from main import simulate_monty_hall

st.title(":zap: monty_hall_simulator")

st.image("../image/image.png", width=700)

number_of_game=st.number_input("Number of Simulations",
                min_value=1, max_value=100000, value=100)

col1,col2 = st.columns(2)
col1.subheader("win percentage if you not switch")
col2.subheader("win percentage if you switch")

chart1 = col1.line_chart(x=None,y=None)
chart2 = col2.line_chart(x=None,y=None)

win_switch = 0
win_no_switch = 0

for i in range(number_of_game):
    num_without_switch,num_with_switch = simulate_monty_hall(1)
    win_no_switch += num_without_switch
    win_switch += num_with_switch
    chart1.add_rows([win_no_switch/(i+1)])
    chart2.add_rows([win_switch/(i+1)])