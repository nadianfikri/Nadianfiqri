class Produk:
    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class Kasir:
    def __init__(self):
        self.cart = []

    def pilih_barang(self):
        nama_barang = input("Masukkan nama barang: ")
        jenis_barang = input("Masukkan jenis barang (minuman/makanan): ")
        harga_barang = float(input("Masukkan harga barang: "))
        return Produk(nama_barang, jenis_barang, harga_barang)

    def input_jumlah_barang(self):
        return int(input("Masukkan jumlah barang: "))

    def memindai_barcode(self, produk):
        print(f"Memindai barcode {produk.nama}...")

    def hitung_total_pembelian(self):
        total = 0
        for produk, jumlah in self.cart:
            total += produk.harga * jumlah
        return total

    def hitung_diskon(self, total_pembelian, diskon):
        return total_pembelian * diskon / 100

    def verifikasi_pembayaran(self, total_harga, metode_pembayaran):
        if metode_pembayaran == "tunai":
            uang_tunai = float(input("Masukkan jumlah uang tunai: "))
            return uang_tunai >= total_harga
        elif metode_pembayaran == "kartu":
            nomor_kartu = input("Masukkan nomor kartu: ")
            return self.verifikasi_dengan_bank(nomor_kartu)
        else:
            return False

    def verifikasi_dengan_bank(self, nomor_kartu):
        print(f"Verifikasi dengan bank untuk kartu {nomor_kartu}...")
        # Logika verifikasi dengan bank
        return True

    def catat_transaksi(self):
        print("Mencatat transaksi...")
        # Logika pencatatan transaksi

    def penanganan_barang(self):
        print("Menangani barang...")
        # Logika penanganan barang

    def struk_pembelian(self, total_harga, diskon):
        print("===== Struk Pembelian =====")
        for produk, jumlah in self.cart:
            print(f"{produk.nama} ({produk.jenis}): {jumlah} x {produk.harga} = {produk.harga * jumlah}")
        print("===========================")
        print(f"Total Harga: {total_harga}")
        print(f"Diskon ({diskon}%): {self.hitung_diskon(total_harga, diskon)}")
        print(f"Total Pembelian Setelah Diskon: {total_harga - self.hitung_diskon(total_harga, diskon)}")
        print("===========================")

    def pesan_terima_kasih(self):
        print("Terima kasih telah berbelanja di Indomaret. Selamat datang kembali!")

# Main program
kasir = Kasir()

while True:
    barang = kasir.pilih_barang()
    jumlah_barang = kasir.input_jumlah_barang()
    kasir.cart.append((barang, jumlah_barang))

    lanjut = input("Tambah barang lain? (y/n): ")
    if lanjut.lower() != 'y':
        break

# Memproses transaksi
for barang, jumlah in kasir.cart:
    kasir.memindai_barcode(barang)

total_pembelian = kasir.hitung_total_pembelian()
diskon = 10  # Misalnya diskon 10%
total_setelah_diskon = total_pembelian - kasir.hitung_diskon(total_pembelian, diskon)

print(f"Total Pembelian: {total_pembelian}")
print(f"Diskon ({diskon}%): {kasir.hitung_diskon(total_pembelian, diskon)}")
print(f"Total Pembelian Setelah Diskon: {total_setelah_diskon}")

metode_pembayaran = input("Pilih metode pembayaran (tunai/kartu): ")
if kasir.verifikasi_pembayaran(total_setelah_diskon, metode_pembayaran):
    kasir.catat_transaksi()
    kasir.penanganan_barang()
    kasir.struk_pembelian(total_setelah_diskon, diskon)
    kasir.pesan_terima_kasih()
else:
    print("Pembayaran tidak valid. Transaksi dibatalkan.")
