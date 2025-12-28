"Analisis Kualitas Udara Tiantan 2013-2017"
Deskripsi: 
Proyek ini bertujuan untuk menganalisis data kualitas udara dan faktor meteorologi yang tercatat di stasiun Tiantan antara Maret 2013 hingga Februari 2017. Analisis yang dilakukan meliputi pembersihan data, eksplorasi pola, dan visualisasi data utuk memahami hubungan antara polutan udara (seperti PM2.5, PM10, SO2, NO2, CO, dan O3) dengan faktor cuaca seperti suhu, kelembapan, dan kecepatan angin. Proyek ini juga menerapkan teknik EDA untuk mengidentifikasi pola dan tren yang ada, serta mengeksplorasi kemungkinan pengaruh faktor-faktor tersebut terhadap kualitas udara.

Dataset yang digunakan :
Dataset yang saya gunakan adalah PRSA Data Tiantan, yang berisi data kualitas udara dan kondisi meteorologi di Tiantan, selama periode 2013–2017. Dataset ini mencakup data waktu, polutan udara, faktor cuaca, dan lokasi pengukuran.

Cara menjalankan dashboard :
karena saya hanya belum menginstall library streamlit maka sebelum itu install streamlit dengan command "pip install streamlit", namun belum bila belum menginstall semua libray maka bisa menggunakan command "pip install streamlit pandas matplotlib seaborn numpy". Lalu pada terminal file app.py ketik "streamlit run app.py" maka otomatis akan langsung ke arahkan ke browser dan file ini berjalan di http://localhost:8501

Deskripsi Data
Jumlah Data: 35,064 observasi
Periode: 2013-2017 
Lokasi: Tiantan
 Kualitas Udara - Status Kritis
Kategori: Tidak Sehat jika berdasarkan standar WHO
Rata-rata PM2.5: 82.2 µg/m³ (melebihi batas aman 25 µg/m³)
Puncak PM2.5: 821 µg/m³ (sangat berbahaya)
Pola Tahunan PM2.5
2013: 83.2 µg/m³
2014: 86.6 µg/m³ (puncak tertinggi)
2015: 82.6 µg/m³
2016: 73.9 µg/m³ (peningkatan signifikan)
2017: 98.4 µg/m³ (peningkatan drastis)
Insight: Terjadi peningkatan yang signifikan di 2016, namun memburuk drastis di 2017.

Pola Musiman Musim Dingin Kritis
Desember: 114.3 µg/m³ (tertinggi)
Januari: 98.3 µg/m³
November: 97.5 µg/m³
Musim Dingin (Nov-Feb): Konsentrasi tertinggi
Musim Panas (Jun-Sep): Konsentrasi terendah
Insight: Polusi udara paling parah di musim dingin, kemungkinan karena pemanasan rumah dan kondisi atmosfer yang stabil.

Korelasi Antar Polutan
PM2.5 vs PM10: 0.893 (sangat kuat) - Partikel halus dan kasar berasal dari sumber sama
PM2.5 vs CO: 0.800 (kuat) - Indikasi polusi pembakaran
PM2.5 vs NO2: 0.663 (sedang-kuat) - Polusi transportasi
PM2.5 vs SO2: 0.397 (sedang) - Polusi industri

Faktor Cuaca
Kecepatan Angin (WSPM): Korelasi negatif (-0.288) - Angin membantu menyebarkan polutan
Suhu (TEMP): Korelasi negatif (-0.150) - Cuaca dingin meningkatkan polusi
Tekanan Udara (PRES): Korelasi positif lemah - Kondisi atmosfer berpengaruh
Hujan (RAIN): Korelasi negatif lemah - Hujan membersihkan udara

Kualitas Data
Missing Values: 1.7-3.2% pada polutan utama
Data Lengkap: 99.9% data cuaca tersedia
