"""Mencatat data lima mahasiswa dan mengklasifikasikan status akademiknya."""


def input_float(pesan, minimum, maksimum):
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"Masukkan angka antara {minimum} dan {maksimum}.")
        except ValueError:
            print("Input harus berupa angka.")


def input_int(pesan, minimum, maksimum):
    while True:
        try:
            nilai = int(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"Masukkan bilangan antara {minimum} dan {maksimum}.")
        except ValueError:
            print("Input harus berupa bilangan bulat.")


def tentukan_status(ipk, sks):
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    if 1.5 <= ipk < 2.0:
        return "Peringatan"
    if ipk < 1.5:
        return "Tidak Aktif"
    return "Peringatan"


def main():
    mahasiswa = []
    print("=== Pencatatan Status Akademik ===")
    for nomor in range(1, 6):
        print(f"\nData mahasiswa ke-{nomor}")
        nim = input("NIM: ").strip()
        while not nim:
            nim = input("NIM tidak boleh kosong. Masukkan NIM: ").strip()
        nama = input("Nama: ").strip()
        while not nama:
            nama = input("Nama tidak boleh kosong. Masukkan nama: ").strip()
        ipk = input_float("IPK (0.0-4.0): ", 0.0, 4.0)
        sks = input_int("SKS (0-24): ", 0, 24)
        mahasiswa.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})

    print("\n" + "=" * 74)
    print(f"{'NIM':<15}{'Nama':<22}{'IPK':>7}{'SKS':>7}  {'Status':<15}")
    print("-" * 74)
    for data in mahasiswa:
        print(f"{data['nim']:<15}{data['nama']:<22}{data['ipk']:>7.2f}"
              f"{data['sks']:>7}  {tentukan_status(data['ipk'], data['sks']):<15}")
    print("=" * 74)


if __name__ == "__main__":
    main()
