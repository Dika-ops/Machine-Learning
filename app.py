import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

try:
    df = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
except FileNotFoundError:
    import numpy as np
    np.random.seed(42)
    data = {
        'PM2.5': np.random.normal(50, 20, 1000),
        'PM10': np.random.normal(80, 30, 1000),
        'SO2': np.random.normal(10, 5, 1000),
        'NO2': np.random.normal(30, 10, 1000),
        'CO': np.random.normal(1, 0.5, 1000),
        'O3': np.random.normal(40, 15, 1000),
        'TEMP': np.random.normal(15, 10, 1000),
        'PRES': np.random.normal(1013, 10, 1000),
        'DEWP': np.random.normal(5, 5, 1000),
        'RAIN': np.random.normal(0, 1, 1000),
        'wd': np.random.choice(['N', 'S', 'E', 'W'], 1000),
        'WSPM': np.random.normal(2, 1, 1000)
    }
    df = pd.DataFrame(data)
st.set_page_config(page_title="Analisis Kualitas Udara Tiantan", layout="wide")

st.title("Analisis Kualitas Udara Tiantan 2013-2017")
st.subheader("Data Kualitas Udara")
if 'year' in df.columns:
    years = sorted(df['year'].unique())
    selected_year = st.selectbox("Pilih Tahun:", ["Semua"] + list(years))
    
    if selected_year != "Semua":
        filtered_df = df[df['year'] == selected_year]
        st.write(f"Menampilkan data untuk tahun {selected_year}:")
        st.write(filtered_df.head())
    else:
        st.write("Menampilkan semua data:")
        st.write(df.head())
else:
    st.write("Kolom 'year' tidak ditemukan. Menampilkan semua data:")
    st.write(df.head())

st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.subheader("Menangani Missing Values")
missing_data = df.isnull().sum()
missing_data_percentage = (missing_data / len(df)) * 100
st.write("Jumlah dan Persentase Nilai Hilang:")
st.write(pd.DataFrame({"Jumlah": missing_data, "Persentase": missing_data_percentage}))

numeric_cols = df.select_dtypes(include=[np.number]).columns
df_filled = df.copy()
df_filled[numeric_cols] = df_filled[numeric_cols].fillna(df_filled[numeric_cols].mean())

st.subheader("Distribusi PM2.5 dan PM10")
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(df_filled['PM2.5'], kde=True, ax=ax[0], color='blue')
ax[0].set_title('Distribusi PM2.5')

sns.histplot(df_filled['PM10'], kde=True, ax=ax[1], color='red')
ax[1].set_title('Distribusi PM10')

st.pyplot(fig)

st.subheader("Matriks Korelasi Antara Variabel")
numeric_df = df_filled.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

st.subheader("Hubungan antara Suhu dan PM2.5")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df_filled, x='TEMP', y='PM2.5', ax=ax)
ax.set_title('Hubungan antara Suhu dan PM2.5')
st.pyplot(fig)

st.sidebar.header("Pilih Analisis")
analysis_option = st.sidebar.radio("Pilih jenis analisis:", ["Statistik Deskriptif", "Visualisasi", "Korelasi"])

if analysis_option == "Statistik Deskriptif":
    st.write(df.describe())
elif analysis_option == "Visualisasi":
    st.write("Pilih plot yang ingin ditampilkan:")
    plot_option = st.selectbox("Pilih plot", ["PM2.5", "PM10", "Suhu vs PM2.5"])
    
    if plot_option == "PM2.5":
        sns.histplot(df_filled['PM2.5'], kde=True)
        st.pyplot()
    elif plot_option == "PM10":
        sns.histplot(df_filled['PM10'], kde=True)
        st.pyplot()
    elif plot_option == "Suhu vs PM2.5":
        sns.scatterplot(data=df_filled, x='TEMP', y='PM2.5')
        st.pyplot()
elif analysis_option == "Korelasi":
    st.write(correlation_matrix)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)