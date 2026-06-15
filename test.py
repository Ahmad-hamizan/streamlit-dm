import streamlit as st

st.title("Prediksi Harga Kendaraan Bekas")
st.write("This is a simple Streamlit app.")

pilihan_kendaraan = st.selectbox("Pilih jenis kendaraan:", ["Mobil", "Motor"])
tahun = st.number_input("Tahun Pembuatan", min_value=1900, max_value=2023, step=1)
jarak_tempuh = st.number_input("Jarak Tempuh (km)", min_value=0, step=1000)
kondisi = st.selectbox("Kondisi Kendaraan:", ["Baik", "Cukup", "Buruk"])
harga = st.number_input("Harga Kendaraan (Rp)", min_value=0, step=10000)
merk_kendaraan = st.text_input("Merk Kendaraan")

if st.button("Prediksi Harga"):
    st.write("Prediksi harga kendaraan:", harga)
    st.write("Jenis Kendaraan:", pilihan_kendaraan)
    st.write("Tahun Pembuatan:", tahun)
    st.write("Jarak Tempuh:", jarak_tempuh, "km")
    st.write("Kondisi Kendaraan:", kondisi)
    st.write("Harga Kendaraan:", harga)
    st.write("Merk Kendaraan:", merk_kendaraan)