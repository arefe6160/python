import streamlit as st
from password_generater import randompaswordgenerator,memorablepaswordgenerator,pingenerator

st.image("./image/banner.png")
st.title("password generator")
option = st.radio("Select Password Type",
                  ("Random Password","Memorable Password","Pin Code"))

if option == "Pin Code":
    length = st.slider("Select Pin Code Length",4,32)
    generator = pingenerator(length)

    password = generator.generate()
    st.write(f"Generated Password: {password}")
elif option == "Random Password":
    length = st.slider("Select Pin Code Length",4,32)
    include_symbol = st.toggle("include symbols")
    include_num = st.toggle("include number")
    generator = randompaswordgenerator(length,include_num,include_symbol)

    password = generator.generate()
    st.write(f"Generated Password: {password}")
elif option == "Memorable Password":
    numofword = st.slider("select number of words:",2,10)
    separator = st.text_input("separator", value='-')
    capitalization= st.toggle("capitalization:")
    generator = memorablepaswordgenerator(numofword, separator, capitalization)

    password = generator.generate()
    st.write(f"Generated Password: {password}")




