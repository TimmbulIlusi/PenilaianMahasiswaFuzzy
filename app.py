import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fuzzy Penilaian Mahasiswa")

st.title("Sistem Fuzzifikasi Penilaian Mahasiswa")

nilai = st.number_input(
    "Masukkan Nilai Mahasiswa (0-100)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Fungsi keanggotaan
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

if st.button("Hitung"):

    r = round(rendah(nilai), 2)
    s = round(sedang(nilai), 2)
    t = round(tinggi(nilai), 2)

    st.subheader("Hasil Fuzzifikasi")

    hasil = pd.DataFrame({
        "Input Nilai":[nilai],
        "Rendah":[r],
        "Sedang":[s],
        "Tinggi":[t]
    })

    st.table(hasil)

    st.write(f"μ Rendah = {r}")
    st.write(f"μ Sedang = {s}")
    st.write(f"μ Tinggi = {t}")

    # Grafik
    x = np.arange(0, 101, 1)

    rendah_y = [rendah(i) for i in x]
    sedang_y = [sedang(i) for i in x]
    tinggi_y = [tinggi(i) for i in x]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(x, rendah_y, label="Rendah")
    ax.plot(x, sedang_y, label="Sedang")
    ax.plot(x, tinggi_y, label="Tinggi")

    ax.axvline(nilai, linestyle="--")

    ax.scatter(nilai, r)
    ax.scatter(nilai, s)
    ax.scatter(nilai, t)

    ax.set_title("Grafik Fungsi Keanggotaan")
    ax.set_xlabel("Nilai")
    ax.set_ylabel("Derajat Keanggotaan")
    ax.set_ylim(0, 1.1)

    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
