# INTEGRASI FRONT END DAN WEB3 #

## TUJUAN PRAKTIKUM ##
1. Mahasiswa memahami arsitektur dApp: frontend, wallet, provider (RPC node), dan smart contract.
2. Mahasiswa mampu menghubungkan aplikasi web ke wallet MetaMask (tombol Connect Wallet).
3. Mahasiswa mampu membaca data on-chain: address pengguna dan saldo ETH.
4. Mahasiswa mampu membaca satu data dari smart contract kelompoknya sendiri melalui ABI.
5. Mahasiswa memahami aturan keamanan wallet: seed phrase dan private key tidak pernah dibagikan.

## LANGKAH PRAKTIKUM ## 

1. Cek Instalasi Node dan Npm (node -v, npm -v)q
2. Jika belum tersedia instal via https://nodejs.org/en/download
3. Bukti node js dan NPM

<img src="image.png" width=55% />

4. Buat folder baru nama dApps
5. Open Terminal dan CD Ke dalam folder tersebut
    ```bash
    mkdir dApps
    cd dApps
    ```
6. Inisialisasi npm
    ```bash
    npm init -y
    ```
7. Install framework Hardhat
npm install --save-dev hardhat
<img src="image-2.png" width=80% /> 

8. Menjalankan hardhart(npx hardhart init)
<img src="image-4.png" width=100% />

9. unduh dan tempatkan file smart contract yang sudah dibuat remix ke folder contract
<img src="image-5.png" width=80% />

10. Compile projek dApps perintah ( npx hardhat compile )
<img src="image-6.png" width=80% />

11. 