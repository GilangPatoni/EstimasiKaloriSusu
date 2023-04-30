import pickle
import streamlit as st

model = pickle.load(open('kalori_susu.sav', 'rb'))

st.title('Estimasi Jumlah Kalori Pada Susu (per 240 ml)')

TotalFat = st.number_input('Masukkan Total Fat (g)')
Sugar = st.number_input('Masukkan Sugar (g)')
TotalCarbohydrate = st.number_input('Masukkan Total Carbohydrate (g)')
Protein = st.number_input('Masukkan Protein (g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[TotalFat, Sugar, TotalCarbohydrate, Protein]]
    )
    st.write ('Estimasi Jumlah Kalori (kCal) : ', predict)