import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("📍 진주시 CCTV 지도")

file_path = "경상남도 진주시_CCTV위치정보_20250501.csv"

data = pd.read_csv(file_path, encoding='cp949')

map_center = [data['위도'].mean(), data['경도'].mean()]
m = folium.Map(location=map_center, zoom_start=13)

for _, row in data.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['설치장소'],
        icon=folium.Icon(color='red', icon='camera')
    ).add_to(m)

st_folium(m, width=700, height=500)
