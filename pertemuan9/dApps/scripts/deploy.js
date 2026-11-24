import { network } from "hardhat";

async function main() {
  const { ethers } = await network.connect();

  const [admin, mahasiswa1] = await ethers.getSigners();

  const Kontrak = await ethers.getContractFactory("CertiChain");
  const kontrak = await Kontrak.deploy();
  await kontrak.waitForDeployment();

  const alamat = await kontrak.getAddress();
  console.log("Alamat Kontrak CertiChain:", alamat);
  console.log("Admin Kampus:", admin.address);

  // Opsional: Terbitkan 1 data contoh awal
  const tx = await kontrak.terbitkanIjazah(
    "IJZ-2026-001",
    "Agung Dwi Jaya",
    "Informatika",
    "QmHashDokumenContoh123456",
    mahasiswa1.address
  );
  await tx.wait();
  console.log("Sertifikat contoh IJZ-2026-001 berhasil diterbitkan!");
}

main().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});