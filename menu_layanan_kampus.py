"""Menu interaktif untuk status mahasiswa, diskon SPP, dan stok barang."""


def baca_float(pesan, minimum, maksimum):
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"Nilai harus antara {minimum} dan {maksimum}.")
        except ValueError:
            print("Masukkan angka yang valid.")


def baca_int(pesan, minimum, maksimum):
    while True:
        try:
            nilai = int(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"Nilai harus antara {minimum} dan {maksimum}.")
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


def baca_yn(pesan):
    while True:
        jawaban = input(pesan).strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("Pilih y atau n.")


def cek_status_mahasiswa():
    print("\n-- Cek Status Mahasiswa --")
    ipk = baca_float("IPK (0.0-4.0): ", 0, 4)
    sks = baca_int("SKS (0-24): ", 0, 24)
    cuti = baca_yn("Sedang cuti? (y/n): ")
    if cuti:
        status = "Cuti"
    elif ipk >= 2 and sks >= 18:
        status = "Aktif"
    elif 1.5 <= ipk < 2:
        status = "Peringatan"
    else:
        status = "Tidak Aktif"
    print(f"Status akademik: {status}")


def hitung_diskon_spp():
    print("\n-- Kalkulator Diskon SPP --")
    biaya = baca_int("Biaya SPP (Rp): ", 0, 10**12)
    anak_karyawan = baca_yn("Anak karyawan? (y/n): ")
    ipk = baca_float("IPK (0.0-4.0): ", 0, 4)
    tepat_waktu = baca_yn("Bayar tepat waktu? (y/n): ")
    if anak_karyawan:
        diskon = 0.25
        kategori = "Anak karyawan"
    elif ipk >= 3.8:
        diskon = 0.20
        kategori = "Prestasi tinggi"
    elif ipk >= 3.5:
        diskon = 0.15
        kategori = "Prestasi baik"
    elif ipk >= 3.0:
        diskon = 0.10
        kategori = "IPK memuaskan"
    else:
        diskon = 0
        kategori = "Tidak ada diskon utama"
    tambahan = 0.05 if tepat_waktu else 0
    total = diskon + tambahan
    potongan = round(biaya * total)
    print(f"Kategori: {kategori}")
    print(f"Diskon total: {total:.0%}")
    print(f"Potongan: Rp{potongan:,}")
    print(f"Biaya akhir: Rp{biaya-potongan:,}")


def cek_stok():
    print("\n-- Cek Peringatan Stok --")
    stok = baca_int("Jumlah stok barang: ", 0, 10**9)
    if stok == 0:
        print("Status HABIS. Prioritas KRITIS. Restock segera.")
    elif stok <= 10:
        print("Status RENDAH. Prioritas TINGGI. Restock secepatnya.")
    elif stok <= 20:
        print("Status PERINGATAN. Prioritas SEDANG. Jadwalkan restock.")
    else:
        print("Status AMAN. Stok mencukupi.")


def main():
    while True:
        print("\n=== Menu Layanan Sistem Informasi Kampus ===")
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            cek_status_mahasiswa()
        elif pilihan == "2":
            hitung_diskon_spp()
        elif pilihan == "3":
            cek_stok()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan 1, 2, 3, atau 0.")


if __name__ == "__main__":
    main()
