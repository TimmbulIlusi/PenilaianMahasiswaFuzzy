# Sistem Fuzzifikasi Penilaian Mahasiswa

Aplikasi sederhana berbasis Streamlit untuk menghitung derajat keanggotaan fuzzy pada nilai mahasiswa menggunakan tiga kategori:

- Rendah
- Sedang
- Tinggi

## Fitur

- Input nilai mahasiswa (0–100)
- Perhitungan derajat keanggotaan fuzzy
- Menampilkan hasil dalam bentuk tabel
- Menampilkan grafik fungsi keanggotaan menggunakan Matplotlib
- Dapat di-deploy ke Streamlit Community Cloud

## Fungsi Keanggotaan

### Rendah

\[
\mu_{rendah}(x)=
\begin{cases}
1, & x \le 25\\
\frac{50-x}{25}, & 25 < x < 50\\
0, & x \ge 50
\end{cases}
\]

### Sedang

\[
\mu_{sedang}(x)=
\begin{cases}
0, & x \le 25 \\
\frac{x-25}{25}, & 25 < x < 50 \\
\frac{75-x}{25}, & 50 \le x < 75 \\
0, & x \ge 75
\end{cases}
\]

### Tinggi

\[
\mu_{tinggi}(x)=
\begin{cases}
0, & x \le 50 \\
\frac{x-50}{25}, & 50 < x < 75 \\
1, & x \ge 75
\end{cases}
\]

## Instalasi

Clone repository:

```bash
git clone https://github.com/username/fuzzy-mahasiswa.git
cd fuzzy-mahasiswa
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
streamlit run app.py
```

## Struktur Proyek

```text
fuzzy-mahasiswa/
│
├── app.py
├── requirements.txt
└── README.md
```

## Contoh Hasil

Input:

```text
60
```

Output:

| Input Nilai | Rendah | Sedang | Tinggi |
|-------------|---------|---------|---------|
| 60 | 0.00 | 0.60 | 0.40 |

## Teknologi yang Digunakan

- Python
- Streamlit
- NumPy
- Pandas
- Matplotlib

## Author

Nama: Hasto Wawandono

Mata Kuliah: Logika Fuzzy
