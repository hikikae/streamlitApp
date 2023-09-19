import pandas as pd
import streamlit

my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title("Papaps")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#Seleccionador
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Escoge cualquier fruta:", list(my_fruit_list.index),['Avocado','Banana'])
#Coloca la lista de donde se selecciona
streamlit.dataframe(my_fruit_list)
