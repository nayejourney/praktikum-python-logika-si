"""Menghitung diskon SPP berdasarkan aturan bisnis pada soal praktikum."""


def input_ya_tidak(pesan):
    while True:
        jawaban = input(pesan).strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("Masukkan y untuk ya atau n untuk tidak.")


def input_ipk():
    while True:
        try:
            ipk = float(input("IPK (0.0-4.0): ").replace(",", "."))
            if 0 <= ipk <= 4:
                return ipk
            print("IPK harus berada pada rentang 0.0 sampai 4.0.")
        except ValueError:
            print("IPK harus berupa angka.")


def main():
    while True:
        try:
            biaya = int(input("Biaya SPP sebelum diskon (Rp): "))
            if biaya >= 0:
                break
            print("Biaya tidak boleh negatif.")
        except ValueError:
            print("Masukkan nominal dalam bilangan bulat.")

    anak_karyawan = input_ya_tidak("Anak karyawan? (y/n): ")
    ipk = input_ipk()
    tepat_waktu = input_ya_tidak("Pembayaran tepat waktu? (y/n): ")

    if anak_karyawan:
        diskon_utama = 0.25
        kategori = "Anak karyawan"
    elif ipk >= 3.8:
        diskon_utama = 0.20
        kategori = "Prestasi IPK >= 3.8"
    elif ipk >= 3.5:
        diskon_utama = 0.15
        kategori = "Prestasi IPK >= 3.5"
    elif ipk >= 3.0:
        diskon_utama = 0.10
        kategori = "Prestasi IPK >= 3.0"
    else:
        diskon_utama = 0.0
        kategori = "Tanpa diskon utama"

    diskon_tambahan = 0.05 if tepat_waktu else 0.0
    total_diskon = diskon_utama + diskon_tambahan
    potongan = round(biaya * total_diskon)
    biaya_final = biaya - potongan

    print("\n=== Rincian Pembayaran SPP ===")
    print(f"Kategori diskon : {kategori}")
    print(f"Diskon utama    : {diskon_utama:.0%}")
    print(f"Diskon tepat waktu: {diskon_tambahan:.0%}")
    print(f"Total diskon    : {total_diskon:.0%}")
    print(f"Potongan biaya  : Rp{potongan:,}")
    print(f"SPP setelah diskon: Rp{biaya_final:,}")


if __name__ == "__main__":
    main()
