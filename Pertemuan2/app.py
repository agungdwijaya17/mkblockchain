import streamlit as st
from pathlib import Path

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="CV Digital Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# LOKASI FOTO
# ==========================================
foto_path = Path(__file__).parent / "mkblockchain" / "Pertemuan2" / "saya.jpeg"
# ==========================================
# SIDEBAR - INPUT DATA DIRI
# ==========================================
st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

nama = st.sidebar.text_input(
    "Nama Lengkap",
    "Agung Dwi Jaya"
)

nim = st.sidebar.text_input(
    "NIM",
    "2530801093"
)

jurusan = st.sidebar.selectbox(
    "Jurusan",
    [
        "Informatika",
        "Sistem Informasi",
        "Teknik Komputer"
    ]
)

deskripsi = st.sidebar.text_area(
    "Deskripsi Singkat",
    "Saya adalah mahasiswa Informatika yang memiliki minat dalam pengembangan aplikasi dan teknologi."
)

# ==========================================
# MAIN AREA
# ==========================================
st.title("🎓 Curriculum Vitae Digital")
st.markdown("---")

# Membuat 2 kolom
kolom_kiri, kolom_kanan = st.columns([2, 1])

# ==========================================
# KOLOM KIRI
# ==========================================
with kolom_kiri:
    st.image("saya.jpeg", width=200)
    st.header(nama)

    st.subheader(
        f"{jurusan} | NIM: {nim}"
    )

    st.write(deskripsi)

    st.markdown("---")

    st.subheader("💻 Keahlian")

    st.write("Python")
    st.progress(85)

    st.write("HTML")
    st.progress(80)

    st.write("C++")
    st.progress(75)

# ==========================================
# KOLOM KANAN - FOTO
# ==========================================
with kolom_kanan:

    if foto_path.exists():

        st.image(
            str(foto_path),
            caption="Foto Profil",
            width=200
        )

# ==========================================
# PENGALAMAN ORGANISASI
# ==========================================
st.markdown("---")

st.subheader("🏢 Pengalaman Organisasi")

pengalaman = st.text_area(
    "Pengalaman",
    "Himpunan Mahasiswa Informatika"
)

st.write(pengalaman)

# ==========================================
# KONTAK
# ==========================================
st.markdown("---")

st.subheader("📬 Hubungi Saya")

with st.expander("Klik untuk melihat detail kontak"):

    st.write(
        "📧 Email: agungdwijaya1712@gmail.com"
    )

    st.write(
        "🔗 LinkedIn: linkedin.com/in/agungdwijaya"
    )

    st.write(
        "🐙 GitHub: github.com/agungdwijaya17"
    )

# ==========================================
# DOWNLOAD DATA CV
# ==========================================
data_cv = (
    f"Nama: {nama}\n"
    f"NIM: {nim}\n"
    f"Jurusan: {jurusan}\n"
    f"Deskripsi: {deskripsi}\n"
    f"Pengalaman Organisasi: {pengalaman}\n"
)

st.download_button(
    label="📥 Download Data CV",
    data=data_cv,
    file_name="CV_Agung_Dwi_Jaya.txt",
    mime="text/plain"
)