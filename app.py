import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Fuzzy Penilaian Mahasiswa",
    page_icon="📚",
    layout="centered"
)

# =====================================
# JUDUL
# =====================================
st.title("📚 Sistem Fuzzifikasi Penilaian Mahasiswa")

st.write("""
Aplikasi ini digunakan untuk menentukan kategori nilai mahasiswa
berdasarkan logika fuzzy.
""")

st.markdown("---")

# =====================================
# INPUT
# =====================================
nilai = st.number_input(
    "Masukkan Nilai Mahasiswa",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# =====================================
# FUNGSI KEANGGOTAAN
# =====================================
def rendah(x):
    if x <= 25:
        return 1
    elif 25 < x < 50:
        return (50 - x) / 25
    else:
        return 0


def sedang(x):
    if x <= 25 or x >= 75:
        return 0
    elif 25 < x < 50:
        return (x - 25) / 25
    elif 50 <= x < 75:
        return (75 - x) / 25
    else:
        return 0


def tinggi(x):
    if x <= 50:
        return 0
    elif 50 < x < 75:
        return (x - 50) / 25
    else:
        return 1


# =====================================
# PROSES
# =====================================
if st.button("Hitung"):

    r = round(rendah(nilai), 2)
    s = round(sedang(nilai), 2)
    t = round(tinggi(nilai), 2)

    # =====================================
    # TABEL HASIL
    # =====================================
    st.subheader("Hasil Fuzzifikasi")

    hasil = pd.DataFrame({
        "Nilai": [nilai],
        "Rendah": [r],
        "Sedang": [s],
        "Tinggi": [t]
    })

    st.table(hasil)

    # =====================================
    # PERHITUNGAN
    # =====================================
    st.subheader("Perhitungan")

    if nilai <= 25:
        st.write("μ Rendah = 1")
    elif nilai < 50:
        st.write(f"μ Rendah = (50 - {nilai}) / 25 = {r}")
    else:
        st.write("μ Rendah = 0")

    if 25 < nilai < 50:
        st.write(f"μ Sedang = ({nilai} - 25) / 25 = {s}")
    elif 50 <= nilai < 75:
        st.write(f"μ Sedang = (75 - {nilai}) / 25 = {s}")
    else:
        st.write(f"μ Sedang = {s}")

    if nilai <= 50:
        st.write("μ Tinggi = 0")
    elif nilai < 75:
        st.write(f"μ Tinggi = ({nilai} - 50) / 25 = {t}")
    else:
        st.write("μ Tinggi = 1")

    # =====================================
    # KATEGORI DOMINAN
    # =====================================
    kategori = {
        "Rendah": r,
        "Sedang": s,
        "Tinggi": t
    }

    hasil_tertinggi = max(kategori, key=kategori.get)

    st.subheader("Kategori Dominan")
    st.success(hasil_tertinggi)

    # =====================================
    # GRAFIK
    # =====================================
    st.subheader("Grafik Fungsi Keanggotaan")

    x = np.arange(0, 101, 1)

    y_rendah = [rendah(i) for i in x]
    y_sedang = [sedang(i) for i in x]
    y_tinggi = [tinggi(i) for i in x]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x, y_rendah, label="Rendah")
    ax.plot(x, y_sedang, label="Sedang")
    ax.plot(x, y_tinggi, label="Tinggi")

    ax.axvline(nilai, linestyle="--")

    ax.scatter(nilai, r)
    ax.scatter(nilai, s)
    ax.scatter(nilai, t)

    ax.set_title("Grafik Penilaian Mahasiswa")
    ax.set_xlabel("Nilai")
    ax.set_ylabel("Derajat Keanggotaan")
    ax.set_ylim(0, 1.1)

    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

    # =====================================
    # KESIMPULAN
    # =====================================
    st.subheader("Kesimpulan")

    st.info(
        f"""
        Nilai {nilai} lebih dekat ke kategori
        {hasil_tertinggi} dengan nilai keanggotaan
        tertinggi sebesar {kategori[hasil_tertinggi]}.
        """
    )
