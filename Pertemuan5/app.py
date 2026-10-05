import streamlit as st
from core import Block, Blockchain


st.set_page_config(
    page_title="Supply Chain Kopi",
    page_icon="☕"
)

st.title("☕ Sistem Pelacakan Rantai Pasok Kopi")


# Membuat blockchain hanya satu kali selama aplikasi berjalan
if "kopi_chain" not in st.session_state:
    st.session_state.kopi_chain = Blockchain()


# Input data pengiriman kopi
data_kopi = st.text_input(
    "Masukkan Data Pengiriman (Misal: '100kg - Petani A'):"
)


# Tombol untuk melakukan mining
if st.button("⛏️ Mine Block (Tambah Data)"):

    if data_kopi:

        # Menentukan index blok baru
        new_index = len(st.session_state.kopi_chain.chain)

        # Membuat blok baru
        new_block = Block(
            new_index,
            data_kopi,
            ""
        )

        # Menampilkan proses loading ketika mining
        with st.spinner("Sedang mencari Hash yang tepat (Mining)..."):

            st.session_state.kopi_chain.add_block(new_block)

        st.success(
            "Blok berhasil ditambahkan dan diamankan ke dalam rantai!"
        )

st.markdown("---")

if st.button("🔍 Cek Integritas Rantai"):

    if st.session_state.kopi_chain.is_chain_valid():

        st.success(
            "Status Jaringan: AMAN (Rantai Valid)"
        )

    else:

        st.error(
            "Status Jaringan: BAHAYA (Data telah dimanipulasi!)"
        )


st.markdown("---")

st.subheader("📖 Buku Besar (Ledger)")


for block in st.session_state.kopi_chain.chain:

    with st.expander(
        f"Blok #{block.index} - Hash: {block.hash[:15]}..."
    ):

        st.write(f"**Waktu:** {block.timestamp}")

        st.write(f"**Data:** {block.data}")

        # Menampilkan Nonce
        st.write(f"**Nonce (Tebakan):** {block.nonce}")

        # Menampilkan hash sebelumnya
        st.write(f"**Prev Hash:** {block.previous_hash}")

        # Menampilkan hash hasil mining
        st.info(f"**Hash:** {block.hash}")