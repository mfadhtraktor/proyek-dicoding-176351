import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("https://raw.githubusercontent.com/mfadhtraktor/proyek-dicoding-176351/refs/heads/main/day.csv")

weathersit_df = day_df.groupby("weathersit").cnt.sum().sort_values(ascending=False).reset_index()

weekday_df = day_df.groupby("weekday").cnt.sum().sort_values(ascending=False).reset_index()

weathersit_df.rename(columns={
    "weathersit": "Kondisi Cuaca",
    "cnt": "Jumlah Penyewaan"
}, inplace=True)
weathersit_df.replace({
    1: "Cerah",
    2: "Berkabut",
    3: "Hujan Ringan"
}, inplace=True)

weekday_df.rename(columns={
    "weekday": "Hari",
    "cnt": "Jumlah Penyewaan"
}, inplace=True)
weekday_df.replace({
    0: "Minggu",
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu"
}, inplace=True)

st.title('Bike Sharing Dataset Dashboard')

tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.header("Bagaimana pengaruh kondisi cuaca terhadap angka penyewaan sepeda?")
    fig = plt.figure(figsize=(7, 3))
    sns.barplot(y="Kondisi Cuaca", x="Jumlah Penyewaan", data=weathersit_df.sort_values(by="Jumlah Penyewaan", ascending=True), orient="h")
    plt.xlabel("Jumlah Penyewaan")
    plt.ylabel("Kondisi Cuaca")
    plt.title("Perbandingan Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca", loc="center", fontsize=15)
    st.pyplot(fig)
    st.markdown("Berdasarkan visualisasi data di atas, kondisi cuaca sangat berpengaruh terhadap jumlah penyewaan sepeda. Dapat dilihat pada kondisi cuaca berkabut jumlah penyewaan sepeda turun lebih dari setengah jumlah penyewaan sepeda pada kondisi cuaca cerah. Pada kondisi cuaca hujan ringan, jumlah penyewaan sepeda turun drastis dibanding saat kondisi cuaca cerah.")


with tab2:
    st.header("Bagaimana pengaruh hari terhadap angka penyewaan sepeda?")
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig2 = plt.figure(figsize=(7, 4))
    sns.barplot(y="Jumlah Penyewaan", x="Hari", data=weekday_df, palette=colors)
    plt.xlabel("Hari")
    plt.ylabel("Jumlah Penyewaan")
    plt.title("Perbandingan Jumlah Penyewaan Sepeda Berdasarkan Hari", loc="center", fontsize=15)
    st.pyplot(fig2)
    st.markdown("Berdasarkan visualisasi data di atas, pengaruh hari pada jumlah penyewaan sepeda hampir tidak memiliki pengaruh. Terlihat grafik yang hampir simetris. Terjadi penurunan angka di hari Minggu sampai Rabu, namun tidak terlalu signifikan. Semua hari memiliki jumlah penyewaan sepeda di angka empat ratus ribu lebih.")
