import streamlit as st

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="CV Digital Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# SIDEBAR - INPUT DATA DIRI
st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

# Komponen input teks
nama = st.sidebar.text_input(
    "Nama Lengkap",
    "Agung Dwi Jaya "
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

#komponen upload file (gambar)
FOTO = st.sidebar.file_uploader("Unggah Foto Profil", type=["jpg", "jpeg", "png"])

deskripsi = st.sidebar.text_area(
    "Deskripsi Singkat",
    "Saya adalah mahasiswa Informatika yang memiliki minat dalam pengembangan aplikasi dan teknologi."
)

# MAIN AREA
st.title("🎓 Curriculum Vitae Digital")
st.markdown("---") #memmbuat garis horizontal

# Membuat 2 kolom
kolom_kiri, kolom_kanan = st.columns([2, 1])

# KOLOM KIRI
with kolom_kiri:
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

# KOLOM KANAN - FOTO
with kolom_kanan:
    # menampilkan foto jika user mengunggahnya
    if FOTO is not None:
        st.image(FOTO, caption="Foto Profil", use_column_width=True)
    else:
     st.sidebar.image("mkblockchain/Pertemuan2/Foto Agung.png", width=200)
        
# PENGALAMAN ORGANISASI
st.markdown("---")
st.subheader("🏢 Pengalaman Organisasi")
pengalaman = st.text_area(
    "Pengalaman",
    "Himpunan Mahasiswa Informatika"
)
st.write(pengalaman)

# KONTAK
st.markdown("---")
st.subheader("📬 Hubungi Saya")
with st.expander("Klik untuk melihat detail kontak"):
    st.write(
        f"📧 Email: "
        f"{nama.lower().replace(' ', '')}@agungdwijaya1712@gmail.com"
    )
    st.write(
        "🔗 LinkedIn: "
        + "nama.lower().replace(" ", "")agungdwijaya"
    )
    st.write(
        "🐙 GitHub: "
        + "nama.lower().replace(" ", "")agungdwijaya17"
    )

# DOWNLOAD DATA CV
data_cv = (
    f"Nama: {nama}\n"
    f"NIM: {nim}\n"
    f"Jurusan: {jurusan}\n"
    f"Deskripsi: {deskripsi}\n"
)

st.download_button(
    label="📥 Download Data CV",
    data=data_cv,
    file_name="CV_Agung_Dwi_Jaya.txt",
    mime="text/plain"
)