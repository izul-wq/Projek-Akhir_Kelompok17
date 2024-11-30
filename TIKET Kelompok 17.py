def welcome_message(title):
    style = "-" * (len(title) + 8)
    print(style)
    print(f"--- {title} ---")
    print(style)

kuota_tiket = {"VIP": 15, "REGULER": 30, "EKONOMI": 40}
harga_tiket = {"VIP": 100000, "REGULER": 75000, "EKONOMI": 50000}
MAX_TIKET = 5

pesanan = {}

def daftar_tiket():
    print("\nDaftar Tiket:")
    for i in kuota_tiket:
        print(f"{i} - Kuota: {kuota_tiket[i]}, Harga: Rp{harga_tiket[i]}")

def pembelian_tiket():
    nama = input("\nMasukkan nama anda: ")
    if nama in pesanan:
        print("Nama sudah memiliki pesanan. Silakan ubah atau hapus pesanan.")
        return

    print("\nPilihan kategori tiket:")
    for kategori in harga_tiket:
        print(f"- {kategori}")

    kategori_tiket = input("Masukkan kategori tiket: ").upper()
    if kategori_tiket not in kuota_tiket:
        print("Kategori tidak valid!")
        return

    jumlah_tiket = int(input(f"Masukkan jumlah tiket (maksimal {MAX_TIKET}): "))
    if jumlah_tiket > kuota_tiket[kategori_tiket]:
        print("Kuota tidak mencukupi!")
        return

    if jumlah_tiket > MAX_TIKET:
        print(f"Jumlah tiket tidak boleh melebihi {MAX_TIKET} tiket!")
        return

    total_harga = jumlah_tiket * harga_tiket[kategori_tiket]
    pesanan[nama] = {"kategori": kategori_tiket, "jumlah": jumlah_tiket, "total": total_harga, "status": "Belum Dibayar"}
    kuota_tiket[kategori_tiket] -= jumlah_tiket

    print(f"\nPesanan berhasil ditambahkan untuk {nama}. Total yang harus dibayar: Rp{total_harga}")

def lihat_pesanan():
    if not pesanan:
        print("\nBelum ada pesanan.")
        return
    print("\nDaftar Pesanan:")
    for nama, data in pesanan.items():
        print(f"- Nama: {nama}, Kategori: {data['kategori']}, Jumlah: {data['jumlah']}, Total: Rp{data['total']}, Status: {data['status']}")

def daftar_belum_bayar():
    belum_bayar = {nama: data for nama, data in pesanan.items() if data["status"] == "Belum Dibayar"}
    if not belum_bayar:
        print("\nTidak ada pesanan yang belum dibayar.")
        return None
    print("\nDaftar Pesanan Belum Dibayar:")
    for nama, data in belum_bayar.items():
        print(f"- Nama: {nama}, Kategori: {data['kategori']}, Jumlah: {data['jumlah']}, Total: Rp{data['total']}")
    return belum_bayar

def ubah_pesanan():
    belum_bayar = daftar_belum_bayar()
    if not belum_bayar:
        return

    nama = input("\nMasukkan nama pemesan yang ingin diubah: ")
    if nama not in pesanan:
        print("Nama tidak ditemukan!")
        return

    kategori_lama = pesanan[nama]["kategori"]
    jumlah_lama = pesanan[nama]["jumlah"]
    kuota_tiket[kategori_lama] += jumlah_lama

    print("\nPilihan kategori tiket:")
    for kategori in harga_tiket:
        print(f"- {kategori}")

    kategori_tiket = input("Masukkan kategori tiket baru: ").upper()
    if kategori_tiket not in kuota_tiket:
        print("Kategori tidak valid!")
        kuota_tiket[kategori_lama] -= jumlah_lama
        return

    jumlah_tiket = int(input(f"Masukkan jumlah tiket baru (maksimal {MAX_TIKET}): "))
    if jumlah_tiket > kuota_tiket[kategori_tiket] or jumlah_tiket > MAX_TIKET:
        print("Jumlah tiket melebihi kuota atau batas maksimal!")
        kuota_tiket[kategori_lama] -= jumlah_lama
        return

    total_harga = jumlah_tiket * harga_tiket[kategori_tiket]
    pesanan[nama] = {"kategori": kategori_tiket, "jumlah": jumlah_tiket, "total": total_harga, "status": "Belum Dibayar"}
    kuota_tiket[kategori_tiket] -= jumlah_tiket

    print(f"\nPesanan untuk {nama} berhasil diubah. Total baru: Rp{total_harga}")

def hapus_pesanan():
    belum_bayar = daftar_belum_bayar()
    if not belum_bayar:
        return

    nama = input("\nMasukkan nama pemesan yang ingin dihapus: ")
    if nama not in pesanan:
        print("\nNama tidak ditemukan!")
        return

    kategori = pesanan[nama]["kategori"]
    jumlah = pesanan[nama]["jumlah"]
    kuota_tiket[kategori] += jumlah
    del pesanan[nama]

    print(f"\nPesanan untuk {nama} berhasil dihapus.")

def bayar_pesanan():
    belum_bayar = daftar_belum_bayar()
    if not belum_bayar:
        return

    nama = input("\nMasukkan nama pemesan yang ingin dibayar: ")
    if nama not in pesanan:
        print("\nNama tidak ditemukan!")
        return

    total = pesanan[nama]["total"]
    print(f"\nTotal awal yang harus dibayar: Rp{total}")

    via = input("Anda ingin melakukan pembayaran lewat mana (offline/online): ").lower()
    while via not in ["offline", "online"]:
        via = input("Pilihan tidak valid. Anda ingin melakukan pembayaran lewat mana (offline/online): ").lower()

    if via == "online":
        print("\nAnda memilih pembayaran online. Metode yang tersedia:")
        print("- Dana")
        print("- Gopay")
        print("- BRI")
        print("- BNI")
        print("- BCA")
        pembayaran = input("Pilih metode pembayaran: ").lower()
        while pembayaran not in ["dana", "gopay", "bri", "bni", "bca"]:
            pembayaran = input("Pilihan tidak valid. Pilih metode pembayaran: ").lower()
        
        if pembayaran == "dana":
            pajak = total * 0.02  # Pajak 2%
        if pembayaran == "gopay":
            pajak = total * 0.02  # Pajak 2%
        if pembayaran == "bri":
            pajak = total * 0.03  # Pajak 3%
        if pembayaran == "bni":
            pajak = total * 0.04  # Pajak 4%
        if pembayaran == "bca":
            pajak = total * 0.05  # Pajak 5%
            
        total += pajak
        print(f"\nMetode pembayaran online dikenakan pajak. Jadi totalnya: Rp{int(total)}")
    else:
        print("\nAnda memilih pembayaran offline. Tidak ada pajak tambahan.")

    while True:
        print(f"Total yang harus dibayar: Rp{int(total)}")
        uang = int(input("Masukkan uang Anda: "))
        if uang < total:
            print("Uang tidak mencukupi! Silakan coba lagi.")
        else:
            kembalian = uang - total
            pesanan[nama]["status"] = "Sudah Dibayar"
            print(f"Pembayaran berhasil untuk {nama}. Kembalian: Rp{int(kembalian)}")
            break

def menu():
    while True:
        print("\nMenu utama")
        print("1. Daftar tiket")
        print("2. Tambah pesanan tiket")
        print("3. Lihat daftar pesanan")
        print("4. Ubah pesanan tiket")
        print("5. Hapus pesanan tiket")
        print("6. Bayar pesanan")
        print("7. Keluar")

        pilihan = int(input("\nMasukkan pilihan menu: "))
        if pilihan == 1:
            daftar_tiket()
        elif pilihan == 2:
            pembelian_tiket()
        elif pilihan == 3:
            lihat_pesanan()
        elif pilihan == 4:
            ubah_pesanan()
        elif pilihan == 5:
            hapus_pesanan()
        elif pilihan == 6:
            bayar_pesanan()
        elif pilihan == 7:
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

welcome_message("Hai, kamu mau beli tiket konser?")
menu()