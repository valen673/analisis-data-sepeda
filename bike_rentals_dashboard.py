import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('combined_analysis_results.csv')
day_data = pd.read_csv('day.csv')

st.title('Dashboard Analisis Peminjaman Sepeda 🚲')
st.sidebar.header('Filter Options')
date_range = st.sidebar.date_input("Select date range:", [])

# Jumlah Peminjaman Sepeda Berdasarkan Jangka Waktu
st.header('Jumlah Peminjaman Sepeda Berdasarkan Jangka Waktu')
time_df = df[['Date', 'Total Rentals']].dropna()
time_df['Date'] = pd.to_datetime(time_df['Date'])
if date_range:
    time_df = time_df[(time_df['Date'] >= pd.to_datetime(date_range[0])) &
                      (time_df['Date'] <= pd.to_datetime(date_range[1]))]

fig3, ax3 = plt.subplots()
ax3.plot(time_df['Date'], time_df['Total Rentals'], marker='o', linestyle='-')
ax3.set_xlabel('Tanggal')
ax3.set_ylabel('Jumlah Peminjaman')
ax3.set_title('Jumlah Pinjam Sepeda Dalam Jangka Waktu')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Visualisasi pengaruh cuaca terhadap jumlah peminjaman sepeda
st.header('Pengaruh Cuaca Terhadap Peminjaman Sepeda 🌤️')
weather_df = df[['Weather Condition', 'Average Rentals']].dropna()

fig, ax = plt.subplots()
ax.bar(weather_df['Weather Condition'], weather_df['Average Rentals'], color='skyblue')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Peminjaman Rata-rata')
ax.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
st.pyplot(fig)

# Visualisasi jumlah peminjaman pada hari kerja vs hari libur
st.header('Peminjaman Sepeda Saat Hari Kerja VS Hari Libur 🏢')
workday_rentals = day_data.groupby('workingday')['cnt'].mean().reset_index()
workday_rentals['workingday'] = workday_rentals['workingday'].map({0: 'Holiday/Weekend', 1: 'Working Day'})
workday_rentals.columns = ['Day Type', 'Average Rentals']

fig2, ax2 = plt.subplots()
ax2.bar(workday_rentals['Day Type'], workday_rentals['Average Rentals'], color='green')
ax2.set_xlabel('Tipe Hari')
ax2.set_ylabel('Peminjaman Rata-rata')
ax2.set_title('Rata-rata Peminjaman Sepeda Antara Hari Kerja dan Libur')
st.pyplot(fig2)

st.markdown("""
    <div style="text-align: justify;">
        Berdasarkan hasil visualisasi dari proses analisis data yang dilakukan, dapat disimpulkan 
        bahwa kondisi cuaca sangat mempengaruhi perilaku masyarakat dalam memilih kendaraan khususnya 
        dalam kasus peminjaman sepeda. Masyarakat paling sering menggunakan sepeda ketika cuaca sedang 
        cerah dan sedikit berawan dan paling jarang menggunakan sepeda ketika cuaca sedang hujan atau salju.
        Selain itu masyarakat cenderung lebih sering menggunakan sepeda saat hari kerja dimana sepeda 
        digunakan sebagai alat transportasi untuk berangkat ke tempat pekerjaannya.
    </div>
""", unsafe_allow_html=True)
