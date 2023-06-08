import streamlit
streamlit.title('My parents new healthy dinner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header(' Breakfast')
streamlit.text('Poha/Idli/Dosa/Omlet/Fruit slad')


streamlit.header('Lunch')
streamlit.text('Chawal / Rajjma/Veggi/Papad/Sweets')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
