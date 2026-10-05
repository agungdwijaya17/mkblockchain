import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash

        # Atribut baru: nonce
        self.nonce = 0

        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Nonce ikut dimasukkan dalam perhitungan hash
        value = (   
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )

        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Target hash harus diawali dengan angka 0 sesuai difficulty
        target = "0" * difficulty

        # Melakukan proses mining sampai hash memenuhi target
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(
            f"Block Mined! Nonce: {self.nonce} | Hash: {self.hash}"
        )


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

        # Tingkat kesulitan mining
        self.difficulty = 3

    def create_genesis_block(self):
        return Block(
            0,
            "Genesis Block - Rantai Dimulai",
            "0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Mengambil hash dari blok sebelumnya
        new_block.previous_hash = self.get_latest_block().hash

        # Melakukan proses mining sebelum blok dimasukkan
        new_block.mine_block(self.difficulty)

        # Menambahkan blok ke dalam rantai
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Mengecek apakah ada data yang dimanipulasi
        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Cek apakah hash blok masih sesuai
            if current_block.hash != current_block.calculate_hash():
                return False

            # Cek apakah hubungan dengan blok sebelumnya masih benar
            if current_block.previous_hash != previous_block.hash:
                return False

        return True