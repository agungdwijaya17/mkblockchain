# INTEGRASI FRONT END DAN WEB3 #

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


11. Menjalankan Node untuk mendapatkan aktor dan address (npx hardhat  --> node)
<img src="image-8.png" width=90% />

12. Membuat file deploy.js difolder scripts

<img src="image-11.png" width=90% />

13. Deploy node ke local npx hardhat run scripts/deploy.js --network localhost

<img src="image-9.png" width=90% />

14. Membuat File index.html

<img src="image-10.png" width=60% />

15. Install ekstension meta mask

<img src="image-7.png" width=90% />

16. Login / Create Akun Via Oauth GMail
17. Create Custom Network dengan nama Hardhat Local
18. Import Custom account via private key (Private key di dapat di terminal VScode)
19. Jalankan Index.html (npx serve .)

<img src="image-12.png" width=90% />

20. Hasil sudah Koneksi

<img src="image-13.png" width=90% />