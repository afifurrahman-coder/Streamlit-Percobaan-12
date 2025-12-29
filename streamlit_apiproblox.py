import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Nilai Ujian",
    page_icon="📊",
    layout="wide"
)

# =========================
# DARK MODE STYLING
# =========================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
[data-testid="stMetricValue"] {
    color: #00ffcc;
}
[data-testid="stMetricLabel"] {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR MENU
# =========================
st.sidebar.title("📂 Menu")
menu = st.sidebar.radio(
    "Pilih Halaman",
    ["📊 Dashboard", "👤 Tentang Saya"]
)
st.sidebar.caption("Dashboard Streamlit | Dark Mode")

# =========================
# DATA NILAI UJIAN
# =========================
data = {
    "Mata Kuliah": [
        "Algoritma",
        "Basis Data",
        "Statistika",
        "Pemrograman",
        "Kecerdasan Buatan",
        "Jaringan Komputer",
        "Sistem Operasi"
    ],
    "Nilai Ujian": [78, 85, 90, 88, 92, 80, 87]
}

df = pd.DataFrame(data)

# =========================
# HALAMAN DASHBOARD
# =========================
if menu == "📊 Dashboard":

    # TITLE
    st.title("📊 Dashboard Nilai Ujian Mahasiswa")

    # HEADER & SUBHEADER
    st.header("📈 Visualisasi Nilai Ujian")
    st.subheader("Menggunakan Streamlit dan Python")

    # TEXT
    st.write(
        "Dashboard ini menampilkan data nilai ujian mahasiswa dengan "
        "visualisasi grafik batang dan diagram lingkaran untuk membantu "
        "analisis performa akademik."
    )

    # CAPTION
    st.caption("📌 Data simulasi untuk keperluan pembelajaran")

    # CODE
    st.subheader("💻 Contoh Potongan Kode")
    st.code(
        """
import pandas as pd

data = {
    "Mata Kuliah": ["Algoritma", "Basis Data"],
    "Nilai Ujian": [78, 85]
}

df = pd.DataFrame(data)
""",
        language="python"
    )

    # METRIC
    st.subheader("📌 Ringkasan Nilai")

    col1, col2, col3 = st.columns(3)
    col1.metric("🏆 Nilai Tertinggi", df["Nilai Ujian"].max())
    col2.metric("📊 Rata-rata Nilai", round(df["Nilai Ujian"].mean(), 2))
    col3.metric("⚠️ Nilai Terendah", df["Nilai Ujian"].min())

    # DATAFRAME
    st.subheader("📋 Tabel Nilai Ujian")
    st.dataframe(df, use_container_width=True)

    # =========================
    # CHART BAR
    # =========================
    st.subheader("📊 Grafik Batang Nilai Ujian")

    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(df["Mata Kuliah"], df["Nilai Ujian"])
    ax_bar.set_xlabel("Mata Kuliah")
    ax_bar.set_ylabel("Nilai Ujian")
    ax_bar.set_ylim(0, 100)
    ax_bar.set_title("Grafik Batang Nilai Ujian")
    plt.xticks(rotation=45)

    st.pyplot(fig_bar)

    # =========================
    # CHART PIE
    # =========================
    st.subheader("🥧 Diagram Lingkaran Proporsi Nilai")

    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(
        df["Nilai Ujian"],
        labels=df["Mata Kuliah"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax_pie.set_title("Distribusi Nilai Ujian")

    st.pyplot(fig_pie)

# =========================
# HALAMAN TENTANG SAYA
# =========================
elif menu == "👤 Tentang Saya":

    st.title("👤 Tentang Saya")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("profil.jpeg", caption="Foto Profil", width=220)

    with col2:
        st.header("Data Pribadi")
        st.write("""
        - **Nama** : Afifurrahman  
        - **NIM** : 4232401019  
        - **Jurusan** : Teknik Elektro
        - **Program Studi** : TeknologI Rekayasa Pembangkit Energi           
        - **Universitas** : Politeknik Negeri Batam
        """)

        st.subheader("Deskripsi Singkat")
        st.write(
            "Saya adalah mahasiswa Teknik Elektro yang tertarik pada "
            "pemrograman Python, analisis data, dan pengembangan aplikasi web. "
            "Dashboard ini dibuat sebagai bagian dari pembelajaran Streamlit."
        )

    st.caption("© 2025 | Dashboard Streamlit - Afifurrahman")
