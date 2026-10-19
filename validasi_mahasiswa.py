"""Validasi NIM, IPK, SKS, dan semester mahasiswa."""


def validasi_data(nim, ipk, sks, semester):
    errors = []

    if not isinstance(nim, str):
        errors.append("NIM harus berupa teks.")
    elif len(nim) != 10 or not nim.isdigit():
        errors.append("NIM harus terdiri dari 10 digit angka.")
    else:
        tahun = int(nim[:4])
        if not 2000 <= tahun <= 2037:
            errors.append("Tahun pada NIM harus berada pada rentang 2000-2037.")

    if not isinstance(ipk, (int, float)) or isinstance(ipk, bool) or not 0.0 <= ipk <= 4.0:
        errors.append("IPK harus berupa angka pada rentang 0.0-4.0.")

    if not isinstance(sks, int) or isinstance(sks, bool) or not 0 <= sks <= 24:
        errors.append("SKS harus berupa bilangan bulat pada rentang 0-24.")

    if not isinstance(semester, int) or isinstance(semester, bool) or not 1 <= semester <= 14:
        errors.append("Semester harus berupa bilangan bulat pada rentang 1-14.")

    return errors


def input_float(pesan):
    while True:
        try:
            return float(input(pesan).replace(",", "."))
        except ValueError:
            print("Masukkan angka yang valid.")


def input_int(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


def main():
    print("=== Form Validasi Data Mahasiswa ===")
    nim = input("NIM (10 digit): ").strip()
    ipk = input_float("IPK: ")
    sks = input_int("SKS tempuh: ")
    semester = input_int("Semester: ")
    errors = validasi_data(nim, ipk, sks, semester)

    print("\n=== Hasil Validasi ===")
    if errors:
        print(f"Data belum valid. Jumlah masalah: {len(errors)}")
        for nomor, error in enumerate(errors, start=1):
            print(f"{nomor}. {error}")
    else:
        print("Semua data valid dan siap diproses.")


if __name__ == "__main__":
    main()
