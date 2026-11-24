const btnConnect = document.getElementById('btnConnect');
const elAddress = document.getElementById('address');
const elSaldo = document.getElementById('saldo');

btnConnect.addEventListener('click', async () => {
    // 1. Cek apakah MetaMask tersedia
    if (!window.ethereum) {
        alert('MetaMask tidak terdeteksi. Pasang dulu ekstensinya.');
        return;
    }
    try {
        // 2. Minta izin koneksi (pop-up MetaMask)
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // 3. Provider lewat wallet browser, lalu signer
        const provider = new ethers.BrowserProvider(window.ethereum);
        const signer = await provider.getSigner();
        const address = await signer.getAddress();

        // 4. Baca saldo (call — gratis, tanpa gas)
        const balance = await provider.getBalance(address);

        elAddress.innerText = address;
        elSaldo.innerText = ethers.formatEther(balance) + ' ETH';
    } catch (err) {
        // Pengguna menutup/menolak pop-up MetaMask
        alert('Koneksi dibatalkan: ' + err.message);
    }
});

// ===== Pertemuan 10 — Membaca Data Smart Contract =====
// Contract: SupplyChainKopi (file SupplyChainKopi.sol)
// Prasyarat: Connect Wallet dari Pertemuan 9 sudah ada di atas file ini.
// Elemen HTML yang dibutuhkan: #status, #daftar, #jumlah,
// #btnMuat, #btnRefresh (tambah di index.html).

// ---------- Elemen tampilan ----------
const elStatus = document.getElementById("status");
const elDaftar = document.getElementById("daftar");
const elJumlah = document.getElementById("jumlah");

// Label untuk enum StatusKopi: 0=Panen, 1=Diproses, 2=Dikirim, 3=Diterima
const LABEL_STATUS = ["Panen", "Diproses", "Dikirim", "Diterima"];

// ---------- Tahap 1 — ABI sesuai contract asli ----------
// Fungsi baca yang BENAR-BENAR ADA di contract:
//   - totalKopi() -> jumlah batch yang terdaftar
//   - daftarKopi(id) -> struct Kopi (id, namaPetani, beratKg, status, pemilikSaatIni)
const abi = [
    "function totalKopi() view returns (uint256)",
    "function daftarKopi(uint256) view returns (uint256 id, string namaPetani, uint256 beratKg, uint8 status, address pemilikSaatIni)",
];

// ---------- Tahap 2 — Hubungkan Contract ----------
const alamatKontrak = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0"; // [SESUAIKAN: alamat hasil deploy]
const provider = new ethers.BrowserProvider(window.ethereum);
const kontrak = new ethers.Contract(alamatKontrak, abi, provider);

// ---------- Tahap 3 — Baca Satu Data ----------
async function muatStatus() {
    elStatus.innerText = "Memuat...";
    const kopi = await kontrak.daftarKopi(1); // [SESUAIKAN]
    elStatus.innerText =
        `#${kopi.id} — ${kopi.namaPetani} (${kopi.beratKg.toString()} kg) — ${LABEL_STATUS[Number(kopi.status)]}`;
}
document.getElementById("btnMuat").onclick = muatStatus;

// ---------- Tahap 4 — Dashboard Banyak Data (paralel) ----------
// Daftar id dibangun dari totalKopi() — bukan hardcode [1, 2, 3].
async function muatDashboard() {
    elDaftar.innerText = "Memuat...";
    const total = Number(await kontrak.totalKopi());
    if (total === 0) {
        elDaftar.innerText = "Belum ada data panen.";
        return;
    }
    const ids = Array.from({ length: total }, (_, i) => i + 1);
    const hasil = await Promise.all(ids.map((id) => kontrak.daftarKopi(id)));
    elDaftar.innerHTML = hasil.map((kopi) =>
        `<div class="kartu">Batch #${kopi.id}: ${kopi.namaPetani} — ${kopi.beratKg.toString()} kg — ${LABEL_STATUS[Number(kopi.status)]} — ${kopi.pemilikSaatIni}</div>`
    ).join("");
}
document.getElementById("btnRefresh").onclick = muatDashboard;

// ---------- Tahap 5 — Format Nilai dan Penanganan Error ----------
async function muatAman() {
    try {
        const net = await provider.getNetwork();
        if (net.chainId !== 31337n) {
            elStatus.innerText = "Pindah ke jaringan Hardhat Local dulu.";
            return;
        }
        const jumlah = await kontrak.totalKopi(); // [SESUAIKAN]
        elJumlah.innerText = jumlah.toString();
    } catch (e) {
        elStatus.innerText = "Gagal membaca: cek alamat contract dan ABI.";
        console.error(e);
    }
}

// Jalankan pengecekan jaringan + tampilkan jumlah saat halaman dimuat.
muatAman();