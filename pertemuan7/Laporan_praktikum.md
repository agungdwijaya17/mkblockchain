## Logika Smart Contract Lanjutan : (Struct, Mapping, Events, dan Error Handling (Require/Revert)) ##

## A. Tujuan Praktikum ##
1. Mahasiswa mampu memahami dan menerapkan Event pada Solidity untuk mencatat riwayat transaksi secara efisien.
2. Mahasiswa mampu menggunakan Require untuk membangun sistem kontrol akses (Access Control) yang aman.
3. Mahasiswa mampu mengimplementasikan logika pemindahan hak milik (Transfer Ownership) atas suatu aset digital.
4. Mahasiswa mulai merancang dan menulis kode Smart Contract (Versi 1) sesuai dengan studi kasus proyek kelompok masing-masing.

## Tahapan Praktikum ##
1. Buka remix dan 
2. Sesuaikan File SupplyChainKopi.sol dengan modul
3. Membuat event untuk StatusBerubah dan KepemilikanBerpindah  
![alt text](image.png)
4. Membuat Pemicu / emit untuk event-event tersebut pada setiap perubahan status
![alt text](image-2.png)
![alt text](image-1.png)
5. Membuat function updateStatus dan transferKopi
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
6. Uji Coba Konsep
- Daftar Panen Baru
![alt text](image-7.png)
- Transfer Kopi Akun 1 (Petani) Ke Akun 2 (Distributor)
![alt text](image-8.png)
- Transfer Kopi Gagal Akun 1 (Petani) Ke Akun 2 (Distributor)
![alt text](image-9.png)
![alt text](image-10.png)
- Transfer Kopi dari Akun 2 (Distributor) Ke Akun 1
![alt text](image-11.png)
![alt text](image-12.png)